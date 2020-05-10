# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWidget.ui'
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


class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(387, 152)
        self.gridLayout = QGridLayout(LoginWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.teacherRadio = QRadioButton(LoginWidget)
        self.teacherRadio.setObjectName(u"teacherRadio")

        self.gridLayout.addWidget(self.teacherRadio, 1, 2, 1, 1)

        self.quitButton = QPushButton(LoginWidget)
        self.quitButton.setObjectName(u"quitButton")

        self.gridLayout.addWidget(self.quitButton, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.studentRadio = QRadioButton(LoginWidget)
        self.studentRadio.setObjectName(u"studentRadio")

        self.gridLayout.addWidget(self.studentRadio, 1, 1, 1, 1)

        self.loginButton = QPushButton(LoginWidget)
        self.loginButton.setObjectName(u"loginButton")

        self.gridLayout.addWidget(self.loginButton, 2, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(LoginWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.idInput = QLineEdit(LoginWidget)
        self.idInput.setObjectName(u"idInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.idInput)

        self.label_2 = QLabel(LoginWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.pwdInput = QLineEdit(LoginWidget)
        self.pwdInput.setObjectName(u"pwdInput")
        self.pwdInput.setEchoMode(QLineEdit.Password)
        self.pwdInput.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pwdInput)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.changePwdButton = QPushButton(LoginWidget)
        self.changePwdButton.setObjectName(u"changePwdButton")

        self.gridLayout.addWidget(self.changePwdButton, 2, 1, 1, 2)


        self.retranslateUi(LoginWidget)

        QMetaObject.connectSlotsByName(LoginWidget)
    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"Login", None))
        self.teacherRadio.setText(QCoreApplication.translate("LoginWidget", u"&Teacher", None))
        self.quitButton.setText(QCoreApplication.translate("LoginWidget", u"Quit", None))
        self.studentRadio.setText(QCoreApplication.translate("LoginWidget", u"St&udent", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWidget", u"Login", None))
        self.label.setText(QCoreApplication.translate("LoginWidget", u"User ID", None))
        self.label_2.setText(QCoreApplication.translate("LoginWidget", u"Password", None))
        self.pwdInput.setInputMask("")
        self.changePwdButton.setText(QCoreApplication.translate("LoginWidget", u"Change Password", None))
    # retranslateUi

