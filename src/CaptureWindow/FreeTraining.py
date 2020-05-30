from .CaptureWidget import CaptureWidget
from .Ui_FreeTraining import Ui_FreeTraining
from utils.classify import Classifier
from DataManager import tmplmgr
from ResultDialog.ResultDialog import ResultDialog

from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtCore import Slot


class FreeTraining(QMainWindow, Ui_FreeTraining):
    def __init__(self, parent=None):
        super(FreeTraining, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.cw = CaptureWidget(parent=self)
        self.layout.addWidget(self.cw)
        self.cw.sig_stop.connect(self.on_stop)

    
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
        self.close()
        classifier = Classifier()
        target_tmpl_id = classifier.classify(records)
        print(target_tmpl_id)
        tmpl_data = tmplmgr.read_data(target_tmpl_id)
        type_id = tmplmgr.get_type_id(target_tmpl_id)
        r = ResultDialog(records, tmpl_data, type_id, self.parent)
        r.show()
