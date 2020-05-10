# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StudentMainWindow.ui'
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


class Ui_StudentMainWindow(object):
    def setupUi(self, StudentMainWindow):
        if StudentMainWindow.objectName():
            StudentMainWindow.setObjectName(u"StudentMainWindow")
        StudentMainWindow.resize(745, 558)
        self.centralwidget = QWidget(StudentMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comparedLearningButton = QPushButton(self.centralwidget)
        self.comparedLearningButton.setObjectName(u"comparedLearningButton")

        self.gridLayout.addWidget(self.comparedLearningButton, 2, 1, 1, 1)

        self.freeTrainingButton = QPushButton(self.centralwidget)
        self.freeTrainingButton.setObjectName(u"freeTrainingButton")

        self.gridLayout.addWidget(self.freeTrainingButton, 2, 0, 1, 1)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")

        self.gridLayout.addWidget(self.exitButton, 2, 3, 1, 1)

        self.poseLayout = QGridLayout()
        self.poseLayout.setObjectName(u"poseLayout")

        self.gridLayout.addLayout(self.poseLayout, 0, 0, 1, 4)

        self.historyButton = QPushButton(self.centralwidget)
        self.historyButton.setObjectName(u"historyButton")

        self.gridLayout.addWidget(self.historyButton, 2, 2, 1, 1)

        StudentMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StudentMainWindow)

        QMetaObject.connectSlotsByName(StudentMainWindow)
    # setupUi

    def retranslateUi(self, StudentMainWindow):
        StudentMainWindow.setWindowTitle(QCoreApplication.translate("StudentMainWindow", u"MainWindow", None))
        self.comparedLearningButton.setText(QCoreApplication.translate("StudentMainWindow", u"Compared Learning", None))
        self.freeTrainingButton.setText(QCoreApplication.translate("StudentMainWindow", u"&Free Training", None))
        self.exitButton.setText(QCoreApplication.translate("StudentMainWindow", u"&Exit", None))
        self.historyButton.setText(QCoreApplication.translate("StudentMainWindow", u"My History Data", None))
    # retranslateUi

