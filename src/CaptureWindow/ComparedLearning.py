from .CaptureWidget import CaptureWidget
from .Ui_ComparedLearning import Ui_ComparedLearningDialog
from HandPose.HandPose import HandPose
from ResultDialog.ResultDialog import ResultDialog

from PySide2.QtWidgets import QDialog, QWidget, QMessageBox
from PySide2.QtCore import Slot, QTimer

import time


class ComparedLearningDialog(QDialog, Ui_ComparedLearningDialog):
    def __init__(self, data, type_id, parent=None):
        super(ComparedLearningDialog, self).__init__(parent)
        self.setupUi(self)
        self.cw = CaptureWidget(parent=self)
        # self.sig_close.emit()
        self.standard_gesture = data
        self.type_id = type_id
        self.userGestureLayout.addWidget(self.cw)
        self.cw.sig_stop.connect(self.on_stop)

        self.model_timer = QTimer()
        self.standard_it = iter(self.standard_gesture)
        self.standard_graph = HandPose()
        self.standard_pose_container = QWidget.createWindowContainer(
            self.standard_graph.scatter_graph)
        self.standardGestureLayout.addWidget(self.standard_pose_container)
        self.setLayout(self.standardGestureLayout)
        self.model_timer.start(int(1000 / 20))
        self.model_timer.timeout.connect(self.get_model_frame)

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
        rd = ResultDialog(
            records, self.standard_gesture, type_id=self.type_id, parent=self)
        rd.exec_()
        self.close()

    def get_model_frame(self):
        try:
            self.standard_graph.refresh(next(self.standard_it))
        except StopIteration:
            self.standard_it = iter(self.standard_gesture)