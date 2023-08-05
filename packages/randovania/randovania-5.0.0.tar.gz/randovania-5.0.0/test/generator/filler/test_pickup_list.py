from unittest.mock import MagicMock

from randovania.game_description.requirements.requirement_list import RequirementList
from randovania.game_description.requirements.requirement_set import RequirementSet
from randovania.game_description.requirements.resource_requirement import ResourceRequirement
from randovania.game_description.resources import search
from randovania.game_description.resources.resource_info import ResourceCollection
from randovania.generator.filler import pickup_list


def test_requirement_lists_without_satisfied_resources(echoes_game_description, default_echoes_preset,
                                                       echoes_game_patches):
    # Setup
    def item(name):
        return search.find_resource_info_with_long_name(echoes_game_description.resource_database.item, name)

    state = echoes_game_description.game.generator.bootstrap.calculate_starting_state(
        echoes_game_description,
        echoes_game_patches,
        default_echoes_preset.configuration)
    state.resources.add_resource_gain([
        (item("Seeker Launcher"), 1),
        (item("Space Jump Boots"), 1),
    ])
    uncollected_resources = []
    possible_sets = [
        RequirementSet([
            RequirementList([
                ResourceRequirement.simple(item("Dark Visor")),
                ResourceRequirement.create(item("Missile"), 5, False),
                ResourceRequirement.simple(item("Seeker Launcher")),
            ]),
            RequirementList([
                ResourceRequirement.simple(item("Screw Attack")),
                ResourceRequirement.simple(item("Space Jump Boots")),
            ]),
            RequirementList([
                ResourceRequirement.simple(item("Power Bomb")),
                ResourceRequirement.simple(item("Boost Ball")),
            ]),
        ]),
        RequirementSet([
            RequirementList([
                ResourceRequirement.simple(item("Power Bomb")),
                ResourceRequirement.simple(item("Boost Ball")),
            ]),
            RequirementList([
                ResourceRequirement.simple(item("Spider Ball")),
                ResourceRequirement.simple(item("Boost Ball")),
            ]),
        ]),
    ]

    # Run
    result = pickup_list._requirement_lists_without_satisfied_resources(
        state, possible_sets, uncollected_resources
    )

    # Assert
    assert result == {
        RequirementList([
            ResourceRequirement.simple(item("Dark Visor")),
            ResourceRequirement.create(item("Missile"), 5, False),
        ]),
        RequirementList([
            ResourceRequirement.simple(item("Screw Attack")),
        ]),
        RequirementList([
            ResourceRequirement.simple(item("Power Bomb")),
            ResourceRequirement.simple(item("Boost Ball")),
        ]),
        RequirementList([
            ResourceRequirement.simple(item("Spider Ball")),
            ResourceRequirement.simple(item("Boost Ball")),
        ]),
    }


def test_get_pickups_that_solves_unreachable(echoes_game_description, mocker):
    def item(name):
        return search.find_resource_info_with_long_name(echoes_game_description.resource_database.item, name)

    mock_req_lists: MagicMock = mocker.patch(
        "randovania.generator.filler.pickup_list._requirement_lists_without_satisfied_resources")

    collection = ResourceCollection.with_database(echoes_game_description.resource_database)
    pickups_left = []
    reach = MagicMock()
    reach.state.resources = collection
    reach.state.energy = 100
    possible_set = MagicMock()
    reach.unreachable_nodes_with_requirements.return_value = {"foo": possible_set}
    uncollected_resource_nodes = [MagicMock()]
    resource = MagicMock()
    uncollected_resource_nodes[0].resource_gain_on_collect.return_value = [(resource, 1)]

    mock_req_lists.return_value = {
        RequirementList([
            ResourceRequirement.simple(item("Dark Visor")),
            ResourceRequirement.create(item("Missile"), 5, False),
        ]),
        RequirementList([
            ResourceRequirement.simple(item("Screw Attack")),
        ]),
        RequirementList([
            ResourceRequirement.simple(item("Power Bomb")),
            ResourceRequirement.simple(item("Boost Ball")),
        ]),
        RequirementList([
            ResourceRequirement.simple(item("Spider Ball")),
            ResourceRequirement.simple(item("Boost Ball")),
        ]),
    }

    # Run
    result = pickup_list.get_pickups_that_solves_unreachable(pickups_left, reach, uncollected_resource_nodes)

    # Assert
    mock_req_lists.assert_called_once_with(reach.state, [possible_set], {resource})
    assert result == tuple()
