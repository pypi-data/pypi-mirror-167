# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'games_tab_blank_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from randovania.gui.widgets.generate_game_widget import *  # type: ignore

class Ui_BlankGameTabWidget(object):
    def setupUi(self, BlankGameTabWidget):
        if not BlankGameTabWidget.objectName():
            BlankGameTabWidget.setObjectName(u"BlankGameTabWidget")
        BlankGameTabWidget.resize(501, 393)
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

        BlankGameTabWidget.addTab(self.tab_intro, "")
        self.tab_generate_game = GenerateGameWidget()
        self.tab_generate_game.setObjectName(u"tab_generate_game")
        BlankGameTabWidget.addTab(self.tab_generate_game, "")
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
        self.faq_scroll_area_contents.setGeometry(QRect(0, 0, 495, 367))
        self.faq_scroll_layout = QGridLayout(self.faq_scroll_area_contents)
        self.faq_scroll_layout.setSpacing(6)
        self.faq_scroll_layout.setContentsMargins(11, 11, 11, 11)
        self.faq_scroll_layout.setObjectName(u"faq_scroll_layout")
        self.faq_label = QLabel(self.faq_scroll_area_contents)
        self.faq_label.setObjectName(u"faq_label")
        self.faq_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_label.setWordWrap(True)

        self.faq_scroll_layout.addWidget(self.faq_label, 0, 0, 1, 1)

        self.faq_scroll_area.setWidget(self.faq_scroll_area_contents)

        self.faq_layout.addWidget(self.faq_scroll_area, 0, 0, 1, 1)

        BlankGameTabWidget.addTab(self.faq_tab, "")

        self.retranslateUi(BlankGameTabWidget)

        BlankGameTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BlankGameTabWidget)
    # setupUi

    def retranslateUi(self, BlankGameTabWidget):
        self.game_cover_label.setText(QCoreApplication.translate("BlankGameTabWidget", u"TextLabel", None))
        self.intro_label.setText(QCoreApplication.translate("BlankGameTabWidget", u"<html><head/><body><p align=\"justify\">The Blank game is used by Randovania to serve as an example of how a game is integrated.</p></body></html>", None))
        self.quick_generate_button.setText(QCoreApplication.translate("BlankGameTabWidget", u"Quick generate", None))
        BlankGameTabWidget.setTabText(BlankGameTabWidget.indexOf(self.tab_intro), QCoreApplication.translate("BlankGameTabWidget", u"Introduction", None))
        BlankGameTabWidget.setTabText(BlankGameTabWidget.indexOf(self.tab_generate_game), QCoreApplication.translate("BlankGameTabWidget", u"Play", None))
        self.faq_label.setText(QCoreApplication.translate("BlankGameTabWidget", u"# updated from code", None))
        BlankGameTabWidget.setTabText(BlankGameTabWidget.indexOf(self.faq_tab), QCoreApplication.translate("BlankGameTabWidget", u"FAQ", None))
        pass
    # retranslateUi

