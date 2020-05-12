from .Ui_TmplMgrWindow import Ui_TmplMgrWindow
from DataManager.TemplateMgr import TmplModel, tmplmgr
from HandPose.TmplViewWidget import TmplViewDialog

from PySide2.QtWidgets import QMainWindow
from PySide2.QtSql import QSqlRelationalDelegate
from PySide2.QtWidgets import QMessageBox

class TmplMgrWindow(QMainWindow, Ui_TmplMgrWindow):
    def __init__(self, parent):
        super(TmplMgrWindow, self).__init__(parent)
        self.setupUi(self)

        self.backButton.clicked.connect(self.close)
        self.removeButton.clicked.connect(self.remove)
        self.saveButton.clicked.connect(self.save)
        self.viewButton.clicked.connect(self.view)

        self.tmpl = TmplModel(self)
        self.tableView.setModel(self.tmpl.model)
        self.delegate = QSqlRelationalDelegate(self.tableView)
        self.tableView.setItemDelegate(self.delegate)
        # self.modifyButton.clicked.connect(self.save)
        
    def save(self):
        res = self.tmpl.model.submitAll()
        if res:
            QMessageBox.information(self, 'Save', 'Save sucessfully.', QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Save', self.tmpl.model.lastError().text(), QMessageBox.Ok)
            # print(self.tmpl.model.lastError().text())

    def remove(self):
        if QMessageBox.question(
                self, 'Remove', self.tr('Really to remove the selected row?'), 
                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            cur_idx = self.tableView.currentIndex().row()
            tmpl_id = self.tmpl.model.record(cur_idx).value('id')
            tmplmgr.remove_data(tmpl_id)
            self.tmpl.model.removeRow(cur_idx)
            if self.tmpl.model.submitAll():
                self.tmpl.refresh()
                QMessageBox.information(self, 'Remove', 'Remove sucessfully.', QMessageBox.Ok)
            else:
                QMessageBox.critical(self, 'Remove', self.tmpl.model.lastError().text(), QMessageBox.Ok)
                # print(self.tmpl.model.lastError().text())
        
    def view(self):
        cur_idx = self.tableView.currentIndex().row()
        tmpl_id = self.tmpl.model.record(cur_idx).value('id')
        data = tmplmgr.read_data(tmpl_id)
        tv = TmplViewDialog(data, self)
        tv.show()
