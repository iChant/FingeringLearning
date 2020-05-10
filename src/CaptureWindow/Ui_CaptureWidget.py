# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CaptureWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_CaptureWidget(object):
    def setupUi(self, CaptureWidget):
        if CaptureWidget.objectName():
            CaptureWidget.setObjectName(u"CaptureWidget")
        CaptureWidget.resize(549, 476)
        self.gridLayout = QGridLayout(CaptureWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.startButton = QPushButton(CaptureWidget)
        self.startButton.setObjectName(u"startButton")

        self.gridLayout.addWidget(self.startButton, 1, 0, 1, 1)

        self.exitButton = QPushButton(CaptureWidget)
        self.exitButton.setObjectName(u"exitButton")

        self.gridLayout.addWidget(self.exitButton, 1, 2, 1, 1)

        self.label = QLabel(CaptureWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.stopButton = QPushButton(CaptureWidget)
        self.stopButton.setObjectName(u"stopButton")

        self.gridLayout.addWidget(self.stopButton, 1, 1, 1, 1)


        self.retranslateUi(CaptureWidget)

        QMetaObject.connectSlotsByName(CaptureWidget)
    # setupUi

    def retranslateUi(self, CaptureWidget):
        CaptureWidget.setWindowTitle(QCoreApplication.translate("CaptureWidget", u"Form", None))
        self.startButton.setText(QCoreApplication.translate("CaptureWidget", u"Start", None))
        self.exitButton.setText(QCoreApplication.translate("CaptureWidget", u"Exit", None))
        self.label.setText(QCoreApplication.translate("CaptureWidget", u"LOADING...", None))
        self.stopButton.setText(QCoreApplication.translate("CaptureWidget", u"Stop", None))
    # retranslateUi

