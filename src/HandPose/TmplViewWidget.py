from .Ui_TmplViewDialog import Ui_TmplViewDialog
from .HandPose import HandPose

from PySide2.QtWidgets import QDialog, QWidget
from PySide2.QtCore import Qt, QTimer

class TmplViewDialog(QDialog, Ui_TmplViewDialog):
    def __init__(self, gesture, parent=None):
        super(TmplViewDialog, self).__init__(parent)
        self.setupUi(self)
        self.gesture = gesture
        self.timer = QTimer()
        self.timer.timeout.connect(self.get_frame_show)

        self.ctrlButton.clicked.connect(self.start_pause)
        self.exitButton.clicked.connect(self.close)
        self.is_paused = False
        self.graph = HandPose()

        self.pose_container = QWidget.createWindowContainer(
            self.graph.scatter_graph)
        self.gridLayout.addWidget(self.pose_container)
        self.setLayout(self.gridLayout)
        self.timer.start(int(1000 / 10))

        self.gesture_iter = iter(self.gesture)

    def start_pause(self):
        if not self.is_paused:
            self.timer.stop()
            self.is_paused = True
        else:
            self.timer.start(int(1000 / 10))
            self.is_paused = False

    def get_frame(self, data):
        self.graph.refresh(data)

    def get_frame_show(self):
        try:
            self.get_frame(next(self.gesture_iter))
            # print('user')
        except StopIteration:
            # print('user stopped')
            self.gesture_iter = iter(self.gesture)