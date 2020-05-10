# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FreeTraining.ui'
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


class Ui_FreeTraining(object):
    def setupUi(self, FreeTraining):
        if FreeTraining.objectName():
            FreeTraining.setObjectName(u"FreeTraining")
        FreeTraining.resize(800, 600)
        self.centralwidget = QWidget(FreeTraining)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.layout = QGridLayout()
        self.layout.setObjectName(u"layout")

        self.gridLayout_2.addLayout(self.layout, 0, 0, 1, 1)

        FreeTraining.setCentralWidget(self.centralwidget)

        self.retranslateUi(FreeTraining)

        QMetaObject.connectSlotsByName(FreeTraining)
    # setupUi

    def retranslateUi(self, FreeTraining):
        FreeTraining.setWindowTitle(QCoreApplication.translate("FreeTraining", u"Free Training", None))
    # retranslateUi

