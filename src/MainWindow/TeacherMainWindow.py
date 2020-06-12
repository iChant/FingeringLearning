from PySide2.QtWidgets import QMainWindow, QWidget
from PySide2.QtCore import Qt
import os

from DataManager import usermgr
from .Ui_TeacherMainWindow import Ui_TeacherMainWindow
from HandPose.HandPose import HandPose

from CaptureWindow.StandardRec import StandardRec
from DataManager.DataWindow.TmplMgrWindow import TmplMgrWindow


class TeacherMainWindow(QMainWindow, Ui_TeacherMainWindow):
    def __init__(self, parent):
        super(TeacherMainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        icon_path = os.path.join(os.path.dirname(__file__), 'front_icon.npy')
        self.hand_pose = HandPose(path=icon_path)
        self.poseContainer = QWidget.createWindowContainer(
            self.hand_pose.scatter_graph)
        self.poseLayout.addWidget(self.poseContainer)
        self.setLayout(self.poseLayout)
        
        self.standardRecordButton.clicked.connect(self.standard_rec)
        self.tmplMgrButton.clicked.connect(self.fingering_manage)
        self.dataViewerButton.clicked.connect(self.data_viewer)
        self.addUserButton.clicked.connect(self.add_user)
        self.exitButton.clicked.connect(self.on_exit)

    def standard_rec(self):
        s = StandardRec(self)
        s.setWindowModality(Qt.ApplicationModal)
        s.show()
        s.lazy_load()
    
    def fingering_manage(self):
        t = TmplMgrWindow(self)
        t.setWindowModality(Qt.ApplicationModal)
        t.show()
    
    def data_viewer(self):
        pass

    def add_user(self):
        pass

    def on_exit(self):
        self.close()
