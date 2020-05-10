import numpy as np
from fastdtw import fastdtw

def get_feat(ser):
    f = ser.reshape(ser.shape[0], ser.shape[1] * ser.shape[2])
    f1, f2 = f[:, :3], f[:, 3:]
    feat = f2 - np.tile(f1, (1, ser.shape[1] - 1))
    return feat.reshape((ser.shape[0], ser.shape[1] - 1, ser.shape[2]))

def cos_dist(v1, v2):
    return (1 - v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))) / 2

def __dist(f1, f2):
    """
    f1, f2 are all features get from poses, [vec1, vec2, ... , vecn]
    """
    res = 0
    for i in range(f1.shape[0]):
        res += cos_dist(f1[i], f2[i]) ** 2
    return np.sqrt(res)

def running_mean(ser, window_sz=None, axis=None):
    w_sz = ser.shape[0] // 4
    if window_sz is not None:
        w_sz = window_sz
    cumsum = np.cumsum(np.insert(ser, 0, 0, axis=axis), axis=axis)
    return (cumsum[w_sz:] - cumsum[:-w_sz]) / float(w_sz)


def dtw(x, y):
    """
    @param x, y: arrays shaped as (frame_cnt, point_cnt, 3)
                 frame_cnt of x and y can be different.
    @return
    """
    assert x.shape[1] == y.shape[1], 'input ' + \
        'arrays should have same shape[1]'
    #smooth
    x, y = running_mean(x, axis=0), running_mean(y, axis=0)
    p_cnt = x.shape[1]

    feat_x, feat_y = get_feat(x), get_feat(y)
    d, p = fastdtw(feat_x, feat_y, dist=__dist)
    return d, p

    

if __name__ == "__main__":
    from HandPose.HandPose import FINGER_INDEX
    d1 = np.load('c-1.npy')
    d2 = np.load('c-2.npy')
    f1, f2 = get_feat(d1), get_feat(d2)

    t = FINGER_INDEX.THUMB
    thumb1 = np.array([d1[:, i, :] for i in t])
    thumb2 = np.array([d2[:, i, :] for i in t])

    
    # smooth
    f1, f2 = running_mean(f1, axis=0), running_mean(f2, axis=0)

    # get distance and path with fastdtw algo,
    # func dist helps to get the distance from
    # one single pose in the motion serial.
    # d, p = fastdtw(f1, f2, dist=__dist)
    td, tp = dtw(thumb1, thumb2)
    print(td)
    print(tp)
  