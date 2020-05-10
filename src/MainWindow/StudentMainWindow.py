from PySide2.QtWidgets import QMainWindow, QWidget
from PySide2.QtCore import Qt
import os

from DataManager import usermgr
from .Ui_StudentMainWindow import Ui_StudentMainWindow
from HandPose.HandPose import HandPose
from CaptureWindow.FreeTraining import FreeTraining


class StudentMainWindow(QMainWindow, Ui_StudentMainWindow):
    def __init__(self, parent):
        super(StudentMainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.freeTrainingButton.clicked.connect(self.free_training)
        self.comparedLearningButton.clicked.connect(self.compared_learning)
        self.historyButton.clicked.connect(self.history_data)
        self.exitButton.clicked.connect(self.exit)
        icon_path = os.path.join(os.path.dirname(__file__), 'front_icon.npy')
        self.hand_pose = HandPose(path=icon_path)
        self.poseContainer = QWidget.createWindowContainer(
            self.hand_pose.scatter_graph)
        self.poseLayout.addWidget(self.poseContainer)
        self.setLayout(self.poseLayout)

    def free_training(self):
        f = FreeTraining(self)
        f.setWindowModality(Qt.ApplicationModal)
        f.show()

    def history_data(self):
        pass

    def compared_learning(self):
        pass
    
    def exit(self):
        self.close()
