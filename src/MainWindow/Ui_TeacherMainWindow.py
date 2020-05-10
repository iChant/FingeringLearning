# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TeacherMainWindow.ui'
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


class Ui_TeacherMainWindow(object):
    def setupUi(self, TeacherMainWindow):
        if TeacherMainWindow.objectName():
            TeacherMainWindow.setObjectName(u"TeacherMainWindow")
        TeacherMainWindow.resize(859, 558)
        self.centralwidget = QWidget(TeacherMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.standardRecordButton = QPushButton(self.centralwidget)
        self.standardRecordButton.setObjectName(u"standardRecordButton")

        self.gridLayout.addWidget(self.standardRecordButton, 2, 0, 1, 1)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")

        self.gridLayout.addWidget(self.exitButton, 2, 4, 1, 1)

        self.dataViewerButton = QPushButton(self.centralwidget)
        self.dataViewerButton.setObjectName(u"dataViewerButton")

        self.gridLayout.addWidget(self.dataViewerButton, 2, 2, 1, 1)

        self.addUserButton = QPushButton(self.centralwidget)
        self.addUserButton.setObjectName(u"addUserButton")

        self.gridLayout.addWidget(self.addUserButton, 2, 3, 1, 1)

        self.poseLayout = QGridLayout()
        self.poseLayout.setObjectName(u"poseLayout")

        self.gridLayout.addLayout(self.poseLayout, 0, 0, 1, 5)

        self.tmplMgrButton = QPushButton(self.centralwidget)
        self.tmplMgrButton.setObjectName(u"tmplMgrButton")

        self.gridLayout.addWidget(self.tmplMgrButton, 2, 1, 1, 1)

        TeacherMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TeacherMainWindow)

        QMetaObject.connectSlotsByName(TeacherMainWindow)
    # setupUi

    def retranslateUi(self, TeacherMainWindow):
        TeacherMainWindow.setWindowTitle(QCoreApplication.translate("TeacherMainWindow", u"MainWindow", None))
        self.standardRecordButton.setText(QCoreApplication.translate("TeacherMainWindow", u"Standard Fingering Record", None))
        self.exitButton.setText(QCoreApplication.translate("TeacherMainWindow", u"&Exit", None))
        self.dataViewerButton.setText(QCoreApplication.translate("TeacherMainWindow", u"Students' Data View", None))
        self.addUserButton.setText(QCoreApplication.translate("TeacherMainWindow", u"Add a User", None))
        self.tmplMgrButton.setText(QCoreApplication.translate("TeacherMainWindow", u"Fingering Template Manger", None))
    # retranslateUi

