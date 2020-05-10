# from MainWindow.UserLoginDialog import LoginWidget
# # from MainWindow.StudentMainWindow import StudentMainWindow
# from CaptureWindow.CaptureWidget import CaptureWidget
# from PySide2.QtWidgets import QApplication

# import sys

# def foo(res):
#     print(res)

# if __name__ == "__main__":
#     app = QApplication([])
#     w = LoginWidget()
#     w.show()
#     sys.exit(app.exec_())

if __name__ == "__main__":
    from HandPose.HandPose import FINGER_INDEX
    import numpy as np
    from utils.dtw import dtw
    d1 = np.load('c-1.npy')
    d2 = np.load('c-2.npy')

    t = FINGER_INDEX.THUMB
    # thumb1 = np.array([d1[:, i, :] for i in t]).T
    # thumb2 = np.array([d2[:, i, :] for i in t]).T
    thumb1 = d1[:, t, :]
    thumb2 = d2[:, t, :]
    
    # get distance and path with fastdtw algo,
    # func dist helps to get the distance from
    # one single pose in the motion serial.
    # d, p = fastdtw(f1, f2, dist=__dist)
    td, tp = dtw(thumb1, thumb2)
    print(td)
    print(tp)
  


# from DataManager import usermgr


# from utils.dtw import cos_dist
# import numpy as np

# a = np.array([1, 1])
# b = np.array([1, 1])

# print(cos_dist(a, b))