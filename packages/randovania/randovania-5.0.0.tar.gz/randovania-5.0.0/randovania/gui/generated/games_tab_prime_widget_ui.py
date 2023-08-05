# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'games_tab_prime_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from randovania.gui.widgets.generate_game_widget import *  # type: ignore

class Ui_PrimeGameTabWidget(object):
    def setupUi(self, PrimeGameTabWidget):
        if not PrimeGameTabWidget.objectName():
            PrimeGameTabWidget.setObjectName(u"PrimeGameTabWidget")
        PrimeGameTabWidget.resize(438, 393)
        self.tab_intro = QWidget()
        self.tab_intro.setObjectName(u"tab_intro")
        self.intro_layout = QVBoxLayout(self.tab_intro)
        self.intro_layout.setSpacing(6)
        self.intro_layout.setContentsMargins(11, 11, 11, 11)
        self.intro_layout.setObjectName(u"intro_layout")
        self.intro_cover_layout = QHBoxLayout()
        self.intro_cover_layout.setSpacing(6)
        self.intro_cover_layout.setObjectName(u"intro_cover_layout")
        self.game_cover_label = QLabel(self.tab_intro)
        self.game_cover_label.setObjectName(u"game_cover_label")

        self.intro_cover_layout.addWidget(self.game_cover_label)

        self.intro_label = QLabel(self.tab_intro)
        self.intro_label.setObjectName(u"intro_label")
        self.intro_label.setWordWrap(True)

        self.intro_cover_layout.addWidget(self.intro_label)


        self.intro_layout.addLayout(self.intro_cover_layout)

        self.quick_generate_button = QPushButton(self.tab_intro)
        self.quick_generate_button.setObjectName(u"quick_generate_button")

        self.intro_layout.addWidget(self.quick_generate_button)

        self.intro_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.intro_layout.addItem(self.intro_spacer)

        PrimeGameTabWidget.addTab(self.tab_intro, "")
        self.tab_generate_game = GenerateGameWidget()
        self.tab_generate_game.setObjectName(u"tab_generate_game")
        PrimeGameTabWidget.addTab(self.tab_generate_game, "")
        self.faq_tab = QWidget()
        self.faq_tab.setObjectName(u"faq_tab")
        self.faq_layout = QGridLayout(self.faq_tab)
        self.faq_layout.setSpacing(6)
        self.faq_layout.setContentsMargins(11, 11, 11, 11)
        self.faq_layout.setObjectName(u"faq_layout")
        self.faq_layout.setContentsMargins(0, 0, 0, 0)
        self.faq_scroll_area = QScrollArea(self.faq_tab)
        self.faq_scroll_area.setObjectName(u"faq_scroll_area")
        self.faq_scroll_area.setWidgetResizable(True)
        self.faq_scroll_area_contents = QWidget()
        self.faq_scroll_area_contents.setObjectName(u"faq_scroll_area_contents")
        self.faq_scroll_area_contents.setGeometry(QRect(0, 0, 432, 367))
        self.gridLayout_10 = QGridLayout(self.faq_scroll_area_contents)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.faq_label = QLabel(self.faq_scroll_area_contents)
        self.faq_label.setObjectName(u"faq_label")
        self.faq_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_label.setWordWrap(True)

        self.gridLayout_10.addWidget(self.faq_label, 0, 0, 1, 1)

        self.faq_scroll_area.setWidget(self.faq_scroll_area_contents)

        self.faq_layout.addWidget(self.faq_scroll_area, 0, 0, 1, 1)

        PrimeGameTabWidget.addTab(self.faq_tab, "")
        self.hints_tab = QWidget()
        self.hints_tab.setObjectName(u"hints_tab")
        self.hints_tab_layout_4 = QVBoxLayout(self.hints_tab)
        self.hints_tab_layout_4.setSpacing(0)
        self.hints_tab_layout_4.setContentsMargins(11, 11, 11, 11)
        self.hints_tab_layout_4.setObjectName(u"hints_tab_layout_4")
        self.hints_tab_layout_4.setContentsMargins(0, 0, 0, 0)
        self.hints_scroll_area = QScrollArea(self.hints_tab)
        self.hints_scroll_area.setObjectName(u"hints_scroll_area")
        self.hints_scroll_area.setWidgetResizable(True)
        self.hints_scroll_area_contents = QWidget()
        self.hints_scroll_area_contents.setObjectName(u"hints_scroll_area_contents")
        self.hints_scroll_area_contents.setGeometry(QRect(0, 0, 432, 367))
        self.hints_scroll_layout_4 = QVBoxLayout(self.hints_scroll_area_contents)
        self.hints_scroll_layout_4.setSpacing(6)
        self.hints_scroll_layout_4.setContentsMargins(11, 11, 11, 11)
        self.hints_scroll_layout_4.setObjectName(u"hints_scroll_layout_4")
        self.hints_label = QLabel(self.hints_scroll_area_contents)
        self.hints_label.setObjectName(u"hints_label")
        self.hints_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hints_label.setWordWrap(True)

        self.hints_scroll_layout_4.addWidget(self.hints_label)

        self.hints_scroll_area.setWidget(self.hints_scroll_area_contents)

        self.hints_tab_layout_4.addWidget(self.hints_scroll_area)

        PrimeGameTabWidget.addTab(self.hints_tab, "")
        self.hint_item_names_tab = QWidget()
        self.hint_item_names_tab.setObjectName(u"hint_item_names_tab")
        self.hint_item_names_layout_4 = QVBoxLayout(self.hint_item_names_tab)
        self.hint_item_names_layout_4.setSpacing(0)
        self.hint_item_names_layout_4.setContentsMargins(11, 11, 11, 11)
        self.hint_item_names_layout_4.setObjectName(u"hint_item_names_layout_4")
        self.hint_item_names_layout_4.setContentsMargins(0, 0, 0, 0)
        self.hint_item_names_scroll_area = QScrollArea(self.hint_item_names_tab)
        self.hint_item_names_scroll_area.setObjectName(u"hint_item_names_scroll_area")
        self.hint_item_names_scroll_area.setWidgetResizable(True)
        self.hint_item_names_scroll_area.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hint_item_names_scroll_contents = QWidget()
        self.hint_item_names_scroll_contents.setObjectName(u"hint_item_names_scroll_contents")
        self.hint_item_names_scroll_contents.setGeometry(QRect(0, 0, 432, 367))
        self.hint_item_names_scroll_layout_4 = QVBoxLayout(self.hint_item_names_scroll_contents)
        self.hint_item_names_scroll_layout_4.setSpacing(6)
        self.hint_item_names_scroll_layout_4.setContentsMargins(11, 11, 11, 11)
        self.hint_item_names_scroll_layout_4.setObjectName(u"hint_item_names_scroll_layout_4")
        self.hint_item_names_label = QLabel(self.hint_item_names_scroll_contents)
        self.hint_item_names_label.setObjectName(u"hint_item_names_label")
        self.hint_item_names_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hint_item_names_label.setWordWrap(True)

        self.hint_item_names_scroll_layout_4.addWidget(self.hint_item_names_label)

        self.hint_item_names_tree_widget = QTableWidget(self.hint_item_names_scroll_contents)
        if (self.hint_item_names_tree_widget.columnCount() < 4):
            self.hint_item_names_tree_widget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.hint_item_names_tree_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.hint_item_names_tree_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.hint_item_names_tree_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.hint_item_names_tree_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.hint_item_names_tree_widget.setObjectName(u"hint_item_names_tree_widget")
        self.hint_item_names_tree_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.hint_item_names_tree_widget.setSortingEnabled(True)

        self.hint_item_names_scroll_layout_4.addWidget(self.hint_item_names_tree_widget)

        self.hint_item_names_scroll_area.setWidget(self.hint_item_names_scroll_contents)

        self.hint_item_names_layout_4.addWidget(self.hint_item_names_scroll_area)

        PrimeGameTabWidget.addTab(self.hint_item_names_tab, "")

        self.retranslateUi(PrimeGameTabWidget)

        PrimeGameTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PrimeGameTabWidget)
    # setupUi

    def retranslateUi(self, PrimeGameTabWidget):
        self.game_cover_label.setText(QCoreApplication.translate("PrimeGameTabWidget", u"TextLabel", None))
        self.intro_label.setText(QCoreApplication.translate("PrimeGameTabWidget", u"<html><head/><body><p align=\"justify\">Explore Tallon IV, acquiring items as you hunt for the Chozo artifacts. Collect them all to unlock the path to the Impact Crater and Metroid Prime.</p><p align=\"justify\">Scanning the statues in the Artifact Temple will provide hints for each artifact's location. Additionally, the entrance room of the Impact Crater has a hint for the Phazon Suit's location.</p><p align=\"justify\">The default settings skip the frigate tutorial by starting at the Landing Site in Tallon Overworld, shuffle two Charge Beams into the item pool, and require 6 artifacts to unlock the Impact Crater. </p><p align=\"justify\">To get started, use the Quick Generate button to generate a game using the default settings!</p></body></html>", None))
        self.quick_generate_button.setText(QCoreApplication.translate("PrimeGameTabWidget", u"Quick generate", None))
        PrimeGameTabWidget.setTabText(PrimeGameTabWidget.indexOf(self.tab_intro), QCoreApplication.translate("PrimeGameTabWidget", u"Introduction", None))
        PrimeGameTabWidget.setTabText(PrimeGameTabWidget.indexOf(self.tab_generate_game), QCoreApplication.translate("PrimeGameTabWidget", u"Play", None))
        self.faq_label.setText(QCoreApplication.translate("PrimeGameTabWidget", u"# updated from code", None))
        PrimeGameTabWidget.setTabText(PrimeGameTabWidget.indexOf(self.faq_tab), QCoreApplication.translate("PrimeGameTabWidget", u"FAQ", None))
        self.hints_label.setText(QCoreApplication.translate("PrimeGameTabWidget", u"<html><head/><body><p align=\"justify\">In\n"
"                                                Metroid Prime, you can find hints from the following\n"
"                                                sources:</p><p align=\"justify\"><span\n"
"                                                style=\" font-weight:600;\">Artifact Temple</span>:\n"
"                                                Hints for where each of your 12 Artifacts are located.\n"
"                                                In a Multiworld, describes which player has the\n"
"                                                artifacts as well.</p></body></html>\n"
"                                            ", None))
        PrimeGameTabWidget.setTabText(PrimeGameTabWidget.indexOf(self.hints_tab), QCoreApplication.translate("PrimeGameTabWidget", u"Hints", None))
        self.hint_item_names_label.setText(QCoreApplication.translate("PrimeGameTabWidget", u"<html><head/><body><p>When\n"
"                                                items are referenced in a hint, multiple names can be\n"
"                                                used depending on how precise the hint is. The names\n"
"                                                each item can use are the following:</p></body></html>\n"
"                                            ", None))
        ___qtablewidgetitem = self.hint_item_names_tree_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PrimeGameTabWidget", u"Item", None));
        ___qtablewidgetitem1 = self.hint_item_names_tree_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PrimeGameTabWidget", u"Precise Category", None));
        ___qtablewidgetitem2 = self.hint_item_names_tree_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PrimeGameTabWidget", u"General Category", None));
        ___qtablewidgetitem3 = self.hint_item_names_tree_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PrimeGameTabWidget", u"Broad Category", None));
        PrimeGameTabWidget.setTabText(PrimeGameTabWidget.indexOf(self.hint_item_names_tab), QCoreApplication.translate("PrimeGameTabWidget", u"Hint Item Names", None))
        pass
    # retranslateUi

