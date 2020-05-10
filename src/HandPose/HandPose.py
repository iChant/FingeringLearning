from PySide2.QtDataVisualization import QtDataVisualization
from PySide2.QtGui import QVector3D

import numpy as np


class FINGER_INDEX:
    WRIST = 0
    THUMB_MCP = 1
    THUMB_PIP = 6
    THUMB_DIP = 7
    THUMB_TIP = 8
    INDEX_MCP = 2
    INDEX_PIP = 9
    INDEX_DIP = 10
    INDEX_TIP = 11
    MIDDLE_MCP = 3
    MIDDLE_PIP = 12
    MIDDLE_DIP = 12
    MIDDLE_TIP = 14
    RING_MCP = 4
    RING_PIP = 15
    RING_DIP = 16
    RING_TIP = 17
    PINKY_MCP = 5
    PINKY_PIP = 18
    PINKY_DIP = 19
    PINKY_TIP = 20
    
    THUMB = [THUMB_MCP, THUMB_PIP, THUMB_DIP, THUMB_TIP]
    INDEX = [INDEX_MCP, INDEX_PIP, INDEX_DIP, INDEX_TIP]
    MIDDLE = [MIDDLE_MCP, MIDDLE_PIP, MIDDLE_DIP, MIDDLE_TIP]
    RING = [RING_MCP, RING_PIP, RING_DIP, RING_TIP]
    PINKY = [PINKY_MCP, PINKY_PIP, PINKY_DIP, PINKY_TIP]


class HandPose:
    def __init__(self, data=None, path=None):
        self.scatter_graph = QtDataVisualization.Q3DScatter()
        self.scatter_graph.activeTheme().setType(
            QtDataVisualization.Q3DTheme.ThemeEbony)
        self.scatter_graph.setShadowQuality(
            QtDataVisualization.QAbstract3DGraph.ShadowQualitySoftHigh)
        self.scatter_graph.scene().activeCamera().setCameraPreset(
            QtDataVisualization.Q3DCamera.CameraPresetNone)
        # self.scatter_graph.scene().activeCamera().setXRotation(180)
        # self.scatter_graph.scene().activeCamera().setYRotation(100)
        self.proxy = QtDataVisualization.QScatterDataProxy()
        self.series = QtDataVisualization.QScatter3DSeries(self.proxy)
        self.series.setItemLabelFormat(
            '@xTitle: @xLabel @yTitle: @yLabel @zTitle: @zLabel')
        self.series.setMeshSmooth(True)
        self.scatter_graph.addSeries(self.series)
        self.scatter_graph.axisX().setTitle('X')
        self.scatter_graph.axisY().setTitle('Y')
        self.scatter_graph.axisZ().setTitle('Z')
        self.scatter_graph.axisX().setReversed(True)
        self.scatter_graph.axisY().setReversed(True)
        self.scatter_graph.axisZ().setReversed(True)
        if path is not None:
            data = np.load(path)
        if data is not None:
            self.refresh(data)

    def refresh(self, pose, color=None):
        # self.scatter_graph.seriesList()[0].dataProxy()
        count = self.proxy.itemCount()
        if count == 0:
            for p in pose:
                item = QtDataVisualization.QScatterDataItem()
                item.setPosition(QVector3D(*p))
                self.scatter_graph.seriesList()[0].dataProxy().addItem(item)
        else:
            index = 0
            for p in pose:
                item = QtDataVisualization.QScatterDataItem()
                item.setPosition(QVector3D(*p))
                self.scatter_graph.seriesList()[0].dataProxy().setItem(index, item)
                index += 1