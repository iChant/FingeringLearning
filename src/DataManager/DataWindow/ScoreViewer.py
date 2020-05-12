from .Ui_ScoreMgrWindow import Ui_ScoreMgrWindow
from DataManager.ScoreMgr import ScoreModel, scoremgr
from HandPose.TmplViewWidget import TmplViewDialog
from DataManager import usermgr

from PySide2.QtWidgets import QMainWindow
from PySide2.QtSql import QSqlRelationalDelegate
from PySide2.QtWidgets import QMessageBox


class ScoreMgrWindow(QMainWindow, Ui_ScoreMgrWindow):
    def __init__(self, fil=None, parent=None):
        super(ScoreMgrWindow, self).__init__(parent)
        self.setupUi(self)

        print(fil)
        self.model = ScoreModel(fil=fil, parent=self)
        self.tableView.setModel(self.model.model)
        self.delegate = QSqlRelationalDelegate(self.tableView)
        self.tableView.setItemDelegate(self.delegate)