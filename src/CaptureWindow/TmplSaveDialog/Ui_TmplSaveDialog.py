# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TmplSaveDialog.ui'
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


class Ui_TmplSaveDialog(object):
    def setupUi(self, TmplSaveDialog):
        if TmplSaveDialog.objectName():
            TmplSaveDialog.setObjectName(u"TmplSaveDialog")
        TmplSaveDialog.setWindowModality(Qt.WindowModal)
        TmplSaveDialog.resize(400, 92)
        self.formLayout = QFormLayout(TmplSaveDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(TmplSaveDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.buttonBox = QDialogButtonBox(TmplSaveDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.buttonBox)

        self.comboBox = QComboBox(TmplSaveDialog)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)


        self.retranslateUi(TmplSaveDialog)
        self.buttonBox.accepted.connect(TmplSaveDialog.accept)
        self.buttonBox.rejected.connect(TmplSaveDialog.reject)

        QMetaObject.connectSlotsByName(TmplSaveDialog)
    # setupUi

    def retranslateUi(self, TmplSaveDialog):
        TmplSaveDialog.setWindowTitle(QCoreApplication.translate("TmplSaveDialog", u"Save", None))
        self.label.setText(QCoreApplication.translate("TmplSaveDialog", u"Type", None))
    # retranslateUi

