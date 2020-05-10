# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TmplMgrWindow.ui'
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


class Ui_TmplMgrWindow(object):
    def setupUi(self, TmplMgrWindow):
        if TmplMgrWindow.objectName():
            TmplMgrWindow.setObjectName(u"TmplMgrWindow")
        TmplMgrWindow.resize(800, 600)
        self.centralwidget = QWidget(TmplMgrWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 4)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout.addWidget(self.saveButton, 1, 0, 1, 1)

        self.viewButton = QPushButton(self.centralwidget)
        self.viewButton.setObjectName(u"viewButton")

        self.gridLayout.addWidget(self.viewButton, 1, 1, 1, 1)

        self.removeButton = QPushButton(self.centralwidget)
        self.removeButton.setObjectName(u"removeButton")

        self.gridLayout.addWidget(self.removeButton, 1, 2, 1, 1)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout.addWidget(self.backButton, 1, 3, 1, 1)

        TmplMgrWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TmplMgrWindow)

        QMetaObject.connectSlotsByName(TmplMgrWindow)
    # setupUi

    def retranslateUi(self, TmplMgrWindow):
        TmplMgrWindow.setWindowTitle(QCoreApplication.translate("TmplMgrWindow", u"Template Manager", None))
        self.saveButton.setText(QCoreApplication.translate("TmplMgrWindow", u"Save", None))
        self.viewButton.setText(QCoreApplication.translate("TmplMgrWindow", u"View", None))
        self.removeButton.setText(QCoreApplication.translate("TmplMgrWindow", u"Remove", None))
        self.backButton.setText(QCoreApplication.translate("TmplMgrWindow", u"Back", None))
    # retranslateUi

