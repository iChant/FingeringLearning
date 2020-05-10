from .CaptureWidget import CaptureWidget
from .Ui_FreeTraining import Ui_FreeTraining

from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot


class FreeTraining(QMainWindow, Ui_FreeTraining):
    def __init__(self, parent=None):
        super(FreeTraining, self).__init__(parent)
        self.setupUi(self)
        self.cw = CaptureWidget(parent=self)
        self.layout.addWidget(self.cw)
        self.cw.sig_stop.connect(self.on_stop)

    def on_stop(self, records):
        print(len(records))
        self.close()
