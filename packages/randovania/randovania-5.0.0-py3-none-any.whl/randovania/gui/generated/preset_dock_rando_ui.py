# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preset_dock_rando.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_PresetDockRando(object):
    def setupUi(self, PresetDockRando):
        if not PresetDockRando.objectName():
            PresetDockRando.setObjectName(u"PresetDockRando")
        PresetDockRando.resize(476, 628)
        self.centralWidget = QWidget(PresetDockRando)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setMaximumSize(QSize(16777215, 16777215))
        self.main_layout = QVBoxLayout(self.centralWidget)
        self.main_layout.setSpacing(6)
        self.main_layout.setContentsMargins(11, 11, 11, 11)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area = QScrollArea(self.centralWidget)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_contents = QWidget()
        self.scroll_area_contents.setObjectName(u"scroll_area_contents")
        self.scroll_area_contents.setGeometry(QRect(0, 0, 474, 626))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_area_contents.sizePolicy().hasHeightForWidth())
        self.scroll_area_contents.setSizePolicy(sizePolicy)
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_contents)
        self.scroll_area_layout.setSpacing(6)
        self.scroll_area_layout.setContentsMargins(11, 11, 11, 11)
        self.scroll_area_layout.setObjectName(u"scroll_area_layout")
        self.scroll_area_layout.setContentsMargins(1, 1, 1, 0)
        self.settings_group = QGroupBox(self.scroll_area_contents)
        self.settings_group.setObjectName(u"settings_group")
        self.gridLayout = QGridLayout(self.settings_group)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mode_combo = QComboBox(self.settings_group)
        self.mode_combo.addItem("")
        self.mode_combo.addItem("")
        self.mode_combo.addItem("")
        self.mode_combo.setObjectName(u"mode_combo")

        self.gridLayout.addWidget(self.mode_combo, 0, 1, 1, 1)

        self.mode_label = QLabel(self.settings_group)
        self.mode_label.setObjectName(u"mode_label")

        self.gridLayout.addWidget(self.mode_label, 0, 0, 1, 1)

        self.mode_description = QLabel(self.settings_group)
        self.mode_description.setObjectName(u"mode_description")

        self.gridLayout.addWidget(self.mode_description, 2, 0, 1, 2)

        self.label = QLabel(self.settings_group)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 2)

        self.line = QFrame(self.settings_group)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)


        self.scroll_area_layout.addWidget(self.settings_group)

        self.dock_types_group = QGroupBox(self.scroll_area_contents)
        self.dock_types_group.setObjectName(u"dock_types_group")
        self.verticalLayout = QVBoxLayout(self.dock_types_group)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.desc_layouts = QHBoxLayout()
        self.desc_layouts.setSpacing(6)
        self.desc_layouts.setObjectName(u"desc_layouts")
        self.change_from_desc = QLabel(self.dock_types_group)
        self.change_from_desc.setObjectName(u"change_from_desc")
        self.change_from_desc.setTextFormat(Qt.MarkdownText)
        self.change_from_desc.setWordWrap(True)

        self.desc_layouts.addWidget(self.change_from_desc)

        self.change_to_desc = QLabel(self.dock_types_group)
        self.change_to_desc.setObjectName(u"change_to_desc")
        self.change_to_desc.setTextFormat(Qt.MarkdownText)
        self.change_to_desc.setWordWrap(True)

        self.desc_layouts.addWidget(self.change_to_desc)


        self.verticalLayout.addLayout(self.desc_layouts)


        self.scroll_area_layout.addWidget(self.dock_types_group)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.scroll_area_layout.addItem(self.spacer)

        self.scroll_area.setWidget(self.scroll_area_contents)

        self.main_layout.addWidget(self.scroll_area)

        PresetDockRando.setCentralWidget(self.centralWidget)

        self.retranslateUi(PresetDockRando)

        QMetaObject.connectSlotsByName(PresetDockRando)
    # setupUi

    def retranslateUi(self, PresetDockRando):
        PresetDockRando.setWindowTitle(QCoreApplication.translate("PresetDockRando", u"Door Locks", None))
        self.settings_group.setTitle(QCoreApplication.translate("PresetDockRando", u"Settings", None))
        self.mode_combo.setItemText(0, QCoreApplication.translate("PresetDockRando", u"Vanilla", None))
        self.mode_combo.setItemText(1, QCoreApplication.translate("PresetDockRando", u"Two-way", None))
        self.mode_combo.setItemText(2, QCoreApplication.translate("PresetDockRando", u"One-way", None))

        self.mode_label.setText(QCoreApplication.translate("PresetDockRando", u"Randomization Type", None))
        self.mode_description.setText(QCoreApplication.translate("PresetDockRando", u"Original door locks.", None))
        self.label.setText(QCoreApplication.translate("PresetDockRando", u"Only Vanilla is compatible with multiworld sessions.", None))
        self.dock_types_group.setTitle(QCoreApplication.translate("PresetDockRando", u"Door Types", None))
        self.change_from_desc.setText(QCoreApplication.translate("PresetDockRando", u"**Doors to Change**\n"
"\n"
"Which door locks can be changed.", None))
        self.change_to_desc.setText(QCoreApplication.translate("PresetDockRando", u"**Change Doors To**\n"
"\n"
"Which locks a door can be changed to.", None))
    # retranslateUi

