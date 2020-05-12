from MainWindow.UserLoginDialog import LoginWidget
from PySide2.QtWidgets import QApplication

import sys


if __name__ == "__main__":
    app = QApplication([])
    w = LoginWidget()
    w.show()
    sys.exit(app.exec_())
