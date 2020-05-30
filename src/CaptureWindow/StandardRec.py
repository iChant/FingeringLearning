from .CaptureWidget import CaptureWidget
from .Ui_FreeTraining import Ui_FreeTraining
from DataManager import tmplmgr
from .TmplSaveDialog.TmplSaveDialog import TmplSaveDialog

from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot


class StandardRec(QMainWindow, Ui_FreeTraining):
    def __init__(self, parent=None):
        super(StandardRec, self).__init__(parent)
        self.setupUi(self)
        self.cw = CaptureWidget(parent=self)
        self.layout.addWidget(self.cw)
        self.cw.sig_stop.connect(self.on_stop)
        self.cw.sig_close.connect(self.close)
        self.setWindowTitle('Standard Recorder')

    def lazy_load(self):
        try:
            self.cw.lazy_load()
        except RuntimeError as re:
            QMessageBox.critical(
                self, 
                'ERROR', 'Camera not available, please check if camera is plugged in!', 
                QMessageBox.Ok)
            self.close()

    def on_stop(self, records):
        save_dialog = TmplSaveDialog(self)
        if save_dialog.exec_():
            t = save_dialog.get_save_type()
            tmplmgr.save_tmpl(records, type_name=t)
            self.close()
