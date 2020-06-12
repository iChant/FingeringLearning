from .Ui_ResultDialog import Ui_ResultDialog
from HandPose.HandPose import HandPose
from HandPose.HandPose import *
from utils.dtw import get_dtw
from DataManager import scoremgr, usermgr

from PySide2.QtWidgets import QDialog, QWidget, QMessageBox
from PySide2.QtCore import QTimer

import time


class ResultDialog(QDialog, Ui_ResultDialog):
    def __init__(self, user_gesture, standard_gesture, type_id, parent=None):
        super(ResultDialog, self).__init__(parent)
        self.setupUi(self)

        self.time_warped = False
        self.type_id = type_id
        self.user_stopped = False
        self.standard_stopped = False
        self.standard_timer = QTimer()
        self.standard_timer.timeout.connect(self.get_standard_frame)
        self.user_timer = QTimer()
        self.user_timer.timeout.connect(self.get_user_frame)
        self.user_gesture = user_gesture
        self.standard_gesture = standard_gesture
        self.standard_timer.start(int(1000 / 10))
        self.user_timer.start(int(1000 / 10))
        self.standard_it = iter(self.standard_gesture)
        self.user_it = iter(self.user_gesture)

        self.is_paused = False
        self.pauseButton.clicked.connect(self.start_pause)
        self.backButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.save)

        # if res[]
        self.user_graph = HandPose()
        self.standard_graph = HandPose()

        self.user_pose_container = QWidget.createWindowContainer(
            self.user_graph.scatter_graph)
        self.userLayout.addWidget(self.user_pose_container)
        self.setLayout(self.userLayout)

        self.standard_pose_container = QWidget.createWindowContainer(
            self.standard_graph.scatter_graph)
        self.standardLayout.addWidget(self.standard_pose_container)
        self.setLayout(self.standardLayout)

        self.dist_too_large = False

        t1 = time.time()
        self.res = get_dtw(self.user_gesture, self.standard_gesture)
        t2 = time.time()
        print('calc time: {}'.format(t2 - t1))
        self.set_dist(self.res)
        self.tipLabel.setEnabled(True)
        self.set_tips(self.res)
        self.timeWarpingButton.toggled.connect(self.warp)
        if self.dist_too_large:
            self.timeWarpingButton.setDisabled(True)
        # self.set_table(dists)

    def get_frame(self, graph, data):
        graph.refresh(data)

    def get_standard_frame(self):
        try:
            if not self.standard_stopped:
                if not self.time_warped:
                    self.get_frame(self.standard_graph, next(self.standard_it))
                else:
                    self.get_frame(self.standard_graph, self.standard_gesture[next(self.standard_it)[1]])
        except StopIteration:
            if self.user_stopped:
                self.start_pause()
                self.standard_it = iter(self.standard_gesture)
                self.user_it = iter(self.user_gesture)
            else:
                self.standard_stopped = True
                self.standard_timer.stop()

    def get_user_frame(self):
        try:
            if not self.user_stopped:
                if not self.time_warped:
                    self.get_frame(self.user_graph, next(self.user_it))
                else:
                    self.get_frame(self.user_graph, self.user_gesture[next(self.user_it)[0]])

        except StopIteration:
            if self.standard_stopped:
                self.start_pause()
                self.standard_it = iter(self.standard_gesture)
                self.user_it = iter(self.user_gesture)
            else:
                self.user_stopped = True
                self.user_timer.stop()

    def start_pause(self):
        if self.is_paused:
            self.user_timer.start(int(1000/10))
            self.standard_timer.start(int(1000/10))
            self.pauseButton.setText('Pause')
        else:
            self.user_timer.stop()
            self.standard_timer.stop()
            self.pauseButton.setText('Start')
        self.is_paused = not self.is_paused
        self.standard_stopped = self.is_paused
        self.user_stopped = self.is_paused
        print(self.is_paused)

    def set_dist(self, res):
        self.totalDistLable.setText(str(res['total']))
        self.indexDistLable.setText(str((res['index'])))
        self.thumbDistLable.setText(str(res['thumb']))
        self.middleDistLable.setText(str(res['middle']))
        self.ringDistLable.setText(str(res['ring']))
        self.pinkyDistLable.setText(str(res['pinky']))

    def set_tips(self, res):
        dist_too_large = set()
        for k in res:
            if k in ['total', 'path']:
                continue
            if res[k] <= 90:
                dist_too_large.add(k)

        if res['total'] < 75 or len(dist_too_large) > 2:
            self.dist_too_large = True
            self.tipLabel.setText(
                'Gesture has too large difference from the standard, maybe try once again?')

        elif len(dist_too_large) > 1:
            fingers = ', '.join(dist_too_large)
            self.tipLabel.setText(
                'Fingers {} have difference from the standard. Please pay more attention on these fingers!'.format(fingers))
        elif len(dist_too_large) == 1:
            finger = dist_too_large.pop()
            self.tipLabel.setText(
                'Finger {} has a large difference from the standard. Pay more attention on this finger!'.format(finger))
        else:
            self.tipLabel.setText(
                'Brillient! Your gesture is quite close to the standard gesture!')

    def save(self):
        if scoremgr.add(self.res, usermgr.get_id(), self.type_id):
            QMessageBox.information(self, self.tr('Save'),
                self.tr('Save successfully!'), QMessageBox.Ok)
        else:
            QMessageBox.critical(self, self.tr('Save'), self.tr(
                'ERROR: {}'.format(scoremgr.last_error())), QMessageBox.Ok)

    def warp(self, toggled):
        if toggled:
            self.start_pause()
            self.is_paused = True
            self.standard_stopped = self.is_paused
            self.user_stopped = self.is_paused
            self.user_timer.stop()
            self.standard_timer.stop()
            print(self.res['path'])
            self.standard_it = iter(self.res['path'])
            self.user_it = iter(self.res['path'])
            self.time_warped = True
            # self.user_timer.start(int(1000/10))
            # self.standard_timer.start(int(1000/10))
        else:
            self.start_pause()
            self.is_paused = True
            self.standard_stopped = self.is_paused
            self.user_stopped = self.is_paused
            self.user_timer.stop()
            self.standard_timer.stop()
            self.standard_it = iter(self.standard_gesture)
            self.user_it = iter(self.user_gesture)
            self.time_warped = False
            # self.user_timer.start(int(1000/10))
            # self.standard_timer.start(int(1000/10))
