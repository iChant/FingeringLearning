# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TmplViewWidget.ui'
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


class Ui_TmplViewWidget(object):
    def setupUi(self, TmplViewWidget):
        if TmplViewWidget.objectName():
            TmplViewWidget.setObjectName(u"TmplViewWidget")
        TmplViewWidget.resize(556, 474)
        self.gridLayout_2 = QGridLayout(TmplViewWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.ctrlButton = QPushButton(TmplViewWidget)
        self.ctrlButton.setObjectName(u"ctrlButton")

        self.gridLayout_2.addWidget(self.ctrlButton, 1, 0, 1, 1)

        self.exitButton = QPushButton(TmplViewWidget)
        self.exitButton.setObjectName(u"exitButton")

        self.gridLayout_2.addWidget(self.exitButton, 1, 1, 1, 1)


        self.retranslateUi(TmplViewWidget)

        QMetaObject.connectSlotsByName(TmplViewWidget)
    # setupUi

    def retranslateUi(self, TmplViewWidget):
        TmplViewWidget.setWindowTitle(QCoreApplication.translate("TmplViewWidget", u"View", None))
        self.ctrlButton.setText(QCoreApplication.translate("TmplViewWidget", u"Pause", None))
        self.exitButton.setText(QCoreApplication.translate("TmplViewWidget", u"Exit", None))
    # retranslateUi

