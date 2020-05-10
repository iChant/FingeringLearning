# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TmplViewDialog.ui'
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


class Ui_TmplViewDialog(object):
    def setupUi(self, TmplViewDialog):
        if TmplViewDialog.objectName():
            TmplViewDialog.setObjectName(u"TmplViewDialog")
        TmplViewDialog.resize(647, 515)
        self.gridLayout_2 = QGridLayout(TmplViewDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ctrlButton = QPushButton(TmplViewDialog)
        self.ctrlButton.setObjectName(u"ctrlButton")

        self.gridLayout_2.addWidget(self.ctrlButton, 1, 1, 1, 1)

        self.exitButton = QPushButton(TmplViewDialog)
        self.exitButton.setObjectName(u"exitButton")

        self.gridLayout_2.addWidget(self.exitButton, 1, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 2)


        self.retranslateUi(TmplViewDialog)

        QMetaObject.connectSlotsByName(TmplViewDialog)
    # setupUi

    def retranslateUi(self, TmplViewDialog):
        TmplViewDialog.setWindowTitle(QCoreApplication.translate("TmplViewDialog", u"Viewer", None))
        self.ctrlButton.setText(QCoreApplication.translate("TmplViewDialog", u"Pause", None))
        self.exitButton.setText(QCoreApplication.translate("TmplViewDialog", u"Exit", None))
    # retranslateUi

