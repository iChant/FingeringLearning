# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScoreMgrWindow.ui'
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


class Ui_ScoreMgrWindow(object):
    def setupUi(self, ScoreMgrWindow):
        if ScoreMgrWindow.objectName():
            ScoreMgrWindow.setObjectName(u"ScoreMgrWindow")
        ScoreMgrWindow.resize(800, 600)
        self.centralwidget = QWidget(ScoreMgrWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 2)

        ScoreMgrWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ScoreMgrWindow)

        QMetaObject.connectSlotsByName(ScoreMgrWindow)
    # setupUi

    def retranslateUi(self, ScoreMgrWindow):
        ScoreMgrWindow.setWindowTitle(QCoreApplication.translate("ScoreMgrWindow", u"Score Viewer", None))
    # retranslateUi

