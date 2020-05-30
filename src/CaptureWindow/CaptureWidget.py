from PySide2.QtWidgets import QWidget, QApplication, QMessageBox
from PySide2.QtCore import Qt, QTimer, Slot, Signal
from PySide2.QtGui import QPixmap, QImage

# from Camera import camera
# from estimator.estimator import estimator
from .Ui_CaptureWidget import Ui_CaptureWidget

from multiprocessing import Queue, Process
from PoseEstimator.PoseEstimator import PoseEstimator
from threading import Thread
import numpy as np

class CaptureWidget(QWidget, Ui_CaptureWidget):
    sig_stop = Signal(list)
    sig_close = Signal()
    def __init__(self, parent=None):
        super(CaptureWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.timer = QTimer()
        self.is_recording = False
        self.records = []
        self.q = Queue()
        self.timer.timeout.connect(self.get_pose)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.exitButton.clicked.connect(self.back)
        self.stopButton.setDisabled(True)
        self.timer.start(int(1000/30))
        

    def lazy_load(self):
        self.estimator = PoseEstimator()
        if not self.estimator.is_running:
            self.estimator.start()


    def draw_pose(self, img_show):
        img = QImage(
            img_show, img_show.shape[1], img_show.shape[0], QImage.Format_BGR888)
        self.label.setPixmap(QPixmap.fromImage(img))

    def start(self):
        self.is_recording = True
        self.startButton.setDisabled(True)
        self.stopButton.setDisabled(False)
        self.exitButton.setDisabled(True)

    def stop(self):
        self.is_recording = False
        self.startButton.setDisabled(False)
        self.stopButton.setDisabled(True)
        self.exitButton.setDisabled(False)
        self.estimator.stop()
        self.sig_stop.emit(np.array(self.records))
        # if self.stop_callback is not None:
        #     self.stop_callback(self.records)

    def back(self):
        self.records = []
        self.is_recording = False
        if self.estimator.is_running:
            self.estimator.stop()
        self.close()

    def get_pose(self):
        try:
            results, img_show = self.estimator.get_pose()
            self.draw_pose(img_show)
            if self.is_recording:
                self.records.append(results)
        except:
            pass
    
    def check_record(self):
        if not self.is_recording:
            self.start()
        else:
            self.stop()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_S:
            self.check_record()

    def closeEvent(self, event):
        self.sig_close.emit()