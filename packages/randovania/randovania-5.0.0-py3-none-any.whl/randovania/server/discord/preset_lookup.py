import base64
import io
import json
import logging
import re
import subprocess

import discord
from discord.ui import Button

import randovania
from randovania.layout import preset_describer, layout_description
from randovania.layout.layout_description import LayoutDescription
from randovania.layout.permalink import Permalink, UnsupportedPermalink
from randovania.layout.preset import Preset
from randovania.layout.versioned_preset import VersionedPreset
from randovania.server.discord.bot import RandovaniaBot
from randovania.server.discord.randovania_cog import RandovaniaCog

possible_links_re = re.compile(r'([A-Za-z0-9-_]{8,})')


def _add_preset_description_to_embed(embed: discord.Embed, preset: Preset):
    for category, items in preset_describer.describe(preset):
        embed.add_field(name=category, value="\n".join(items), inline=True)


def _git_describe(randovania_version: bytes) -> str:
    return subprocess.run(
        ["git", "describe", "--tags", randovania_version.hex()],
        check=True, capture_output=True, text=True,
    ).stdout.strip()


def get_version(original_permalink: str, randovania_version: bytes) -> str | None:
    try:
        version_raw = _git_describe(randovania_version)
        version_split = version_raw.split("-")

        is_dev_version = randovania.is_dev_version()

        if len(version_split) > 1:
            # dev version
            if not is_dev_version:
                logging.info("Skipping permalink %s from dev version %s", original_permalink,
                             version_raw)
                return None

            major, minor, revision = version_split[0][1:].split(".")
            version = f"{major}.{int(minor) + 1}.0.dev{version_split[1]}"
        else:
            if is_dev_version:
                logging.info("Skipping permalink %s from stable version %s", original_permalink,
                             version_raw)
                return None
            # Exclude starting `v`
            version = version_split[0][1:]

    except FileNotFoundError:
        return f"(Unknown version: {randovania_version.hex()})"

    except subprocess.CalledProcessError as e:
        logging.info("Unable to describe permalink commit %s: %s", randovania_version.hex(), str(e))
        return None

    return version


async def look_for_permalinks(message: discord.Message):
    embed = None
    multiple_permalinks = False
    view = None

    for word in possible_links_re.finditer(message.content):
        try:
            permalink = Permalink.from_str(word.group(1))
            randovania_version = permalink.randovania_version
            games = [preset.game for preset in permalink.parameters.presets]
            seed_hash = permalink.seed_hash
            error_message = None

        except UnsupportedPermalink as e:
            permalink = None
            randovania_version = e.randovania_version
            games = e.games
            seed_hash = e.seed_hash
            error_message = f"\n\nPermalink incompatible with Randovania {randovania.VERSION}"
            if e.__cause__ is not None:
                error_message += f"\n{e.__cause__}"

        except (ValueError, UnsupportedPermalink):
            # TODO: handle the incorrect version permalink
            continue

        version = get_version(word.group(1), randovania_version)
        if version is None:
            continue

        if embed is not None:
            multiple_permalinks = True
            continue

        if seed_hash is not None:
            pretty_hash = "Seed Hash: {} ({})".format(
                layout_description.shareable_word_hash(seed_hash, games),
                base64.b32encode(seed_hash).decode(),
            )
        else:
            pretty_hash = "Unknown seed hash"

        player_count = len(games)
        embed = discord.Embed(title=f"`{word.group(1)}`",
                              description=f"{player_count} player multiworld permalink")

        if player_count == 1:
            embed.description = f"{games[0].long_name} permalink"
            if permalink is not None:
                _add_preset_description_to_embed(embed, permalink.parameters.get_preset(0))

        embed.description += f" for Randovania {version}\n{pretty_hash}"

        if permalink is not None:
            view = RequestPresetsView()
        else:
            embed.description += error_message

    if embed is not None:
        content = None
        if multiple_permalinks:
            content = "Multiple permalinks found, using only the first."
        await message.reply(content=content, embed=embed, view=view, mention_author=False)


async def reply_for_preset(message: discord.Message, versioned_preset: VersionedPreset):
    try:
        preset = versioned_preset.get_preset()
    except ValueError as e:
        logging.info("Invalid preset '{}' from {}: {}".format(versioned_preset.name,
                                                              message.author.display_name,
                                                              e))
        return

    embed = discord.Embed(title=preset.name,
                          description=preset.description)
    _add_preset_description_to_embed(embed, preset)
    await message.reply(embed=embed, mention_author=False)


async def reply_for_layout_description(message: discord.Message, description: LayoutDescription):
    embed = discord.Embed(
        title=f"Spoiler file for Randovania {description.randovania_version_text}",
    )

    if description.player_count == 1:
        preset = description.get_preset(0)
        embed.description = "{}, with preset {}.\nSeed Hash: {}\nPermalink: {}".format(
            preset.game.long_name, preset.name,
            description.shareable_word_hash,
            description.permalink.as_base64_str,
        )
        _add_preset_description_to_embed(embed, preset)
    else:
        games = {preset.game.long_name for preset in description.all_presets}
        game_names = sorted(games)

        last_game = game_names.pop()
        games_text = ", ".join(game_names)
        if games_text:
            games_text += " and "
        games_text += last_game

        embed.description = "{} player multiworld for {}.\nSeed Hash: {}\nPermalink: {}".format(
            description.player_count,
            games_text,
            description.shareable_word_hash,
            description.permalink.as_base64_str,
        )

    await message.reply(embed=embed, mention_author=False)


class RequestPresetsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Attach presets",
        style=discord.ButtonStyle.secondary,
        custom_id="attach_presets_of_permalink",
    )
    async def button_callback(self, button: Button, interaction: discord.Interaction):
        try:
            title = (await interaction.original_message()).embeds[0].title
            # Trim leading and trailing `s
            permalink = Permalink.from_str(title[1:-1])

        except (IndexError, ValueError, UnsupportedPermalink) as e:
            logging.exception("Unable to find permalink on message that sent attach_presets_of_permalink")
            permalink = None

        files = []

        if permalink is not None:
            for player, preset in enumerate(permalink.parameters.presets):
                data = io.BytesIO()
                VersionedPreset.with_preset(preset).save_to_io(data)
                data.seek(0)
                files.append(
                    discord.File(data, filename=f"Player {player + 1}'s Preset.{VersionedPreset.file_extension()}")
                )

        await interaction.edit_original_message(
            view=None,
            files=files,
        )


class PermalinkLookupCog(RandovaniaCog):
    def __init__(self, configuration: dict, bot: RandovaniaBot):
        self.configuration = configuration
        self.bot = bot

    async def add_commands(self):
        self.bot.add_view(RequestPresetsView())

    @discord.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        for attachment in message.attachments:
            filename: str = attachment.filename
            if filename.endswith(VersionedPreset.file_extension()):
                data = await attachment.read()
                versioned_preset = VersionedPreset(json.loads(data.decode("utf-8")))
                await reply_for_preset(message, versioned_preset)

            elif filename.endswith(LayoutDescription.file_extension()):
                data = await attachment.read()
                description = LayoutDescription.from_json_dict(json.loads(data.decode("utf-8")))
                await reply_for_layout_description(message, description)

        await look_for_permalinks(message)


def setup(bot: RandovaniaBot):
    bot.add_cog(PermalinkLookupCog(bot.configuration, bot))
