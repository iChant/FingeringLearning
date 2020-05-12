# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ComparedLearning.ui'
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


class Ui_ComparedLearningDialog(object):
    def setupUi(self, ComparedLearningDialog):
        if ComparedLearningDialog.objectName():
            ComparedLearningDialog.setObjectName(u"ComparedLearningDialog")
        ComparedLearningDialog.resize(952, 510)
        self.gridLayout_3 = QGridLayout(ComparedLearningDialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.standardGestureLayout = QGridLayout()
        self.standardGestureLayout.setObjectName(u"standardGestureLayout")

        self.gridLayout.addLayout(self.standardGestureLayout, 1, 0, 1, 1)

        self.userGestureLayout = QGridLayout()
        self.userGestureLayout.setObjectName(u"userGestureLayout")

        self.gridLayout.addLayout(self.userGestureLayout, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)


        self.retranslateUi(ComparedLearningDialog)

        QMetaObject.connectSlotsByName(ComparedLearningDialog)
    # setupUi

    def retranslateUi(self, ComparedLearningDialog):
        ComparedLearningDialog.setWindowTitle(QCoreApplication.translate("ComparedLearningDialog", u"Compared Learning", None))
    # retranslateUi

