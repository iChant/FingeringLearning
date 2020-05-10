from PySide2.QtWidgets import QWidget, QButtonGroup
from PySide2.QtWidgets import QMessageBox

from .Ui_LoginWidget import Ui_LoginWidget
from .StudentMainWindow import StudentMainWindow
from .TeacherMainWindow import TeacherMainWindow

from DataManager import usermgr


class LoginType:
    STUDENT = 0
    TEACHER = 1


class LoginWidget(QWidget, Ui_LoginWidget):
    def __init__(self):
        super(LoginWidget, self).__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.login)
        self.quitButton.clicked.connect(self.quit)
        self.login_type = LoginType.STUDENT
        self.radio_group = QButtonGroup(self)
        self.radio_group.addButton(self.studentRadio, 0)
        self.radio_group.addButton(self.teacherRadio, 1)
        self.studentRadio.setChecked(True)
        self.radio_group.buttonToggled.connect(self.toggle_login_type)
        self.pwdInput.returnPressed.connect(self.login)

    def login(self):
        user_id = self.idInput.text()
        pwd = self.pwdInput.text()
        status = usermgr.login(self.login_type, user_id, pwd)
        if status == 0:
            user_name = usermgr.get_name()
            QMessageBox.information(
                self, self.tr('Login Successful'),
                self.tr('Welcome, {}!'.format(user_name)), QMessageBox.Ok)
            # print(m)
            # self.hide()
            self.close()
            m = StudentMainWindow(self) if \
                self.login_type == LoginType.STUDENT else \
                    TeacherMainWindow(self)
            m.show()

        else:
            QMessageBox.critical(
                self, self.tr('Login Failed'),
                self.tr('Wrong ID or password!'), QMessageBox.Ok)

    def toggle_login_type(self, selected_radio: int):
        if selected_radio == self.studentRadio:
            self.login_type = LoginType.STUDENT
        elif selected_radio == self.teacherRadio:
            self.login_type = LoginType.TEACHER
    
    def quit(self):
        self.close()
