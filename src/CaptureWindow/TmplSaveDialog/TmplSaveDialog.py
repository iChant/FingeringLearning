from .Ui_TmplSaveDialog import Ui_TmplSaveDialog
from DataManager.TemplateMgr import type_info

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog
import os
# import numpy as np


DATASET_DIR = 'dataset'


class TmplSaveDialog(QDialog, Ui_TmplSaveDialog):
    def __init__(self, parent=None):
        super(TmplSaveDialog, self).__init__(parent=parent)
        self.setupUi(self)

        self.comboBox.addItems(type_info.get_name_list())
        # self.buttonBox.accepted()
        # self.save_selected = Signal(str)
        # self.cancel_selected = Signal()

    def get_save_type(self):
        return self.comboBox.currentText()
        # self.save_selected.emit(os.path.join(
        #     DATASET_DIR, typename + '-' + str(count)))
        # np.save()

    # def cancel(self):
    #     self.cancel_selected.emit()


# class SaveDialog(QDialog, Ui_Dialog):
#     def __init__(self, parent=None, f=Default(Qt.WindowFlags)):
#         super().__init__(parent=parent, f=f)
