# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TmplSelectDialog.ui'
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


class Ui_TmplSelectDialog(object):
    def setupUi(self, TmplSelectDialog):
        if TmplSelectDialog.objectName():
            TmplSelectDialog.setObjectName(u"TmplSelectDialog")
        TmplSelectDialog.resize(836, 590)
        self.gridLayout = QGridLayout(TmplSelectDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.okButton = QPushButton(TmplSelectDialog)
        self.okButton.setObjectName(u"okButton")

        self.gridLayout.addWidget(self.okButton, 1, 1, 1, 1)

        self.cancelButton = QPushButton(TmplSelectDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.gridLayout.addWidget(self.cancelButton, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.tableView = QTableView(TmplSelectDialog)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 3)


        self.retranslateUi(TmplSelectDialog)

        QMetaObject.connectSlotsByName(TmplSelectDialog)
    # setupUi

    def retranslateUi(self, TmplSelectDialog):
        TmplSelectDialog.setWindowTitle(QCoreApplication.translate("TmplSelectDialog", u"Select", None))
        self.okButton.setText(QCoreApplication.translate("TmplSelectDialog", u"OK", None))
        self.cancelButton.setText(QCoreApplication.translate("TmplSelectDialog", u"Cancel", None))
    # retranslateUi

