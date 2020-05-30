from MainWindow.UserLoginDialog import LoginWidget
from PySide2.QtWidgets import QApplication

from config import ROOT_PATH

import os
import logging
import sys

log_path = os.path.join(ROOT_PATH, 'app.log')

logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d')


if __name__ == "__main__":
    app = QApplication([])
    w = LoginWidget()
    w.show()
    sys.exit(app.exec_())
