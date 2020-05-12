from .Ui_TmplSelectDialog import Ui_TmplSelectDialog
from DataManager.TemplateMgr import TmplModel
from HandPose.TmplViewWidget import TmplViewDialog

from PySide2.QtWidgets import QDialog
from PySide2.QtSql import QSqlRelationalDelegate
from PySide2.QtCore import Signal

import numpy as np

class TmplSelectDialog(QDialog, Ui_TmplSelectDialog):
    submitted = Signal(int)
    def __init__(self, parent):
        super(TmplSelectDialog, self).__init__(parent)
        self.setupUi(self)

        self.cancelButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.ok)
        self.okButton.setDisabled(True)

        self.tmpl = TmplModel(self)
        self.tableView.setModel(self.tmpl.model)
        self.delegate = QSqlRelationalDelegate(self.tableView)
        self.tableView.setItemDelegate(self.delegate)

        self.tableView.clicked.connect(self.on_tableView_clicked)
    
    def ok(self):
        row = self.tableView.currentIndex().row()
        tmpl_id = self.tmpl.model.record(row).value('id')
        self.submitted.emit(tmpl_id)
        self.close()
    
    def on_tableView_clicked(self):
        self.okButton.setDisabled(False)