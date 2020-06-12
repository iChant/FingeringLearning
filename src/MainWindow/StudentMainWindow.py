from PySide2.QtWidgets import QMainWindow, QWidget
from PySide2.QtCore import Qt
import os
import time

from DataManager import usermgr
from .Ui_StudentMainWindow import Ui_StudentMainWindow
from HandPose.HandPose import HandPose
from CaptureWindow.FreeTraining import FreeTraining
from CaptureWindow.ComparedLearning import ComparedLearningDialog
from DataManager import tmplmgr
from DataManager.DataWindow.ScoreViewer import ScoreMgrWindow
from DataManager.DataWindow.TmplSelectDialog import TmplSelectDialog


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
        f.lazy_load()

    def history_data(self):
        s = ScoreMgrWindow(
            fil='sid="{}"'.format(usermgr.get_id()), parent=self)
        s.setWindowModality(Qt.ApplicationModal)
        s.show()

    def compared_learning(self):
        select = TmplSelectDialog(self)
        select.submitted.connect(self.compared)
        select.exec_()

    def compared(self, tmpl_id):
        data = tmplmgr.read_data(tmpl_id)
        item = tmplmgr.get(id=tmpl_id)
        type_id = int(list(item.keys())[0])
        r = ComparedLearningDialog(data, type_id, self)
        r.setWindowModality(Qt.ApplicationModal)
        r.show()
        r.lazy_load()

    
    def exit(self):
        self.close()
