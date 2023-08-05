# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preset_echoes_beam_configuration.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_PresetEchoesBeamConfiguration(object):
    def setupUi(self, PresetEchoesBeamConfiguration):
        if not PresetEchoesBeamConfiguration.objectName():
            PresetEchoesBeamConfiguration.setObjectName(u"PresetEchoesBeamConfiguration")
        PresetEchoesBeamConfiguration.resize(466, 454)
        self.centralWidget = QWidget(PresetEchoesBeamConfiguration)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setMaximumSize(QSize(16777215, 16777215))
        self.beam_configuration_tab_layout = QVBoxLayout(self.centralWidget)
        self.beam_configuration_tab_layout.setSpacing(6)
        self.beam_configuration_tab_layout.setContentsMargins(11, 11, 11, 11)
        self.beam_configuration_tab_layout.setObjectName(u"beam_configuration_tab_layout")
        self.beam_configuration_tab_layout.setContentsMargins(4, 4, 4, 0)
        self.beam_configuration_label = QLabel(self.centralWidget)
        self.beam_configuration_label.setObjectName(u"beam_configuration_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beam_configuration_label.sizePolicy().hasHeightForWidth())
        self.beam_configuration_label.setSizePolicy(sizePolicy)
        self.beam_configuration_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.beam_configuration_label.setWordWrap(True)

        self.beam_configuration_tab_layout.addWidget(self.beam_configuration_label)

        self.beam_configuration_group = QGroupBox(self.centralWidget)
        self.beam_configuration_group.setObjectName(u"beam_configuration_group")
        self.beam_configuration_group.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.beam_configuration_group.setFlat(True)
        self.beam_configuration_layout = QGridLayout(self.beam_configuration_group)
        self.beam_configuration_layout.setSpacing(6)
        self.beam_configuration_layout.setContentsMargins(11, 11, 11, 11)
        self.beam_configuration_layout.setObjectName(u"beam_configuration_layout")
        self.beam_configuration_layout.setContentsMargins(0, 0, 0, 0)

        self.beam_configuration_tab_layout.addWidget(self.beam_configuration_group)

        self.beam_configuration_spacer = QSpacerItem(20, 311, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.beam_configuration_tab_layout.addItem(self.beam_configuration_spacer)

        PresetEchoesBeamConfiguration.setCentralWidget(self.centralWidget)

        self.retranslateUi(PresetEchoesBeamConfiguration)

        QMetaObject.connectSlotsByName(PresetEchoesBeamConfiguration)
    # setupUi

    def retranslateUi(self, PresetEchoesBeamConfiguration):
        PresetEchoesBeamConfiguration.setWindowTitle(QCoreApplication.translate("PresetEchoesBeamConfiguration", u"Beam Configuration", None))
        self.beam_configuration_label.setText(QCoreApplication.translate("PresetEchoesBeamConfiguration", u"<html><head/><body><p>Configure what each beam uses as ammo and how much ammo is consumed when shooting it uncharged, charged or with a charge combo.</p><p>Logic always uses the default values.</p><p><span style=\" font-weight:600;\">Known Issue: </span>If you're out of the ammo a beam normally uses, you'll be unable to shoot that beam regardless of what it actually uses to shoot.</p></body></html>", None))
        self.beam_configuration_group.setTitle("")
    # retranslateUi

