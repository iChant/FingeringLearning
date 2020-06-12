import numpy as np
from fastdtw import fastdtw
from HandPose.HandPose import get_feat


# def get_feat(ser):
#     f = ser.reshape(ser.shape[0], ser.shape[1] * ser.shape[2])
#     f1, f2 = f[:, :3], f[:, 3:]
#     feat = f2 - np.tile(f1, (1, ser.shape[1] - 1))
#     return feat.reshape((ser.shape[0], ser.shape[1] - 1, ser.shape[2]))


def cos_dist(v1, v2):
    return (1 - v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))) / 2


def __dist(f1, f2):
    """
    f1, f2 are all features get from poses, [vec_1, vec_2, ... , vec_n],
    """
    res = np.array([cos_dist(f1[i], f2[i]) for i in range(f1.shape[0])])
    aver = np.sqrt((res * res).mean())
    cnt = 0
    # If there is some values that is obviously larger than the average, then
    # these 'obsolete' values would describe the dist between f1 and f2.
    if res[res > aver].shape[0] >= 1:
            # (res.shape[0] == 3 and res[res > aver].shape[0] == 1):
        res = res[res > aver]
    return np.sqrt((res * res).sum() / res.shape[0])



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
    # For serials whose lengths are different too much, 
    # consider that they are different type.
    if abs(x.shape[0] - y.shape[0]) > 90: return 1, None
    assert x.shape[1] == y.shape[1], 'input ' + \
        'arrays should have same shape[1]'
    # smooth
    x, y = running_mean(x, axis=0), running_mean(y, axis=0)
    p_cnt = x.shape[1]

    # feat_x, feat_y = get_feat(x), get_feat(y)
    d, p = fastdtw(x, y, radius=2, dist=__dist)
    d /= min(p[-1][0], p[-1][1])
    # d /= len(p)
    return d, p


def get_dtw(user_gesture, standard_gesture):
    res = {}

    u_total, u_t, u_i, u_m, u_r, u_p = get_feat(user_gesture)
    s_total, s_t, s_i, s_m, s_r, s_p = get_feat(standard_gesture)

    # get distance and record them in res
    res['total'], path = dtw(u_total, s_total)
    res['thumb'], _ = dtw(u_t, s_t)
    res['index'], _ = dtw(u_i, s_i)
    res['middle'], _ = dtw(u_m, s_m)
    res['ring'], _ = dtw(u_r, s_r)
    res['pinky'], _ = dtw(u_p, s_p)

    # convert distance to similarity score
    for k in res:
        res[k] = (1 - res[k]) * 100
        res[k] = int(round(res[k], 4))

    res['path'] = path
    return res


if __name__ == "__main__":
    from HandPose.HandPose import FINGER_INDEX
    d1 = np.load('a-1.npy')
    d2 = np.load('a-2.npy')
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
