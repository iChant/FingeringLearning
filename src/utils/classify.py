from .dtw import get_dtw
from HandPose.HandPose import get_feat

from DataManager import tmplmgr

import numpy as np
import heapq

class Classifier:
    def __init__(self):
        self.tmpls = tmplmgr.get()
    
    def classify(self, data, k=1):
        res = {}
        smallest_idx = {}
        tmpl_id_rec = {}
        # res: {type_id: [scores]}
        # tmpls: {type_id: [file_paths]}
        # smallest_idx records the indice of the k 
        #           smallest items in res, same in tmpls
        for type_id in self.tmpls:
            if type_id not in res:
                res[type_id] = []
                tmpl_id_rec[type_id] = []
            for item in self.tmpls[type_id]:
                tmpl_id, file_path = item[0], item[1]
                tmpl_id_rec[type_id].append(tmpl_id)
                d = np.load(file_path)
                res[type_id].append(get_dtw(data, d)['total'])
            smallest_idx[type_id] = list(
                map(res[type_id].index, heapq.nlargest(k, res[type_id])))
        
        largest_id_v = {}
        largest_id_t = {}
        # smallest_type_id = -1
        for type_id in smallest_idx:
            for i in smallest_idx[type_id]:
                largest_id_v[tmpl_id_rec[type_id][i]] = res[type_id][i]
                largest_id_t[tmpl_id_rec[type_id][i]] = type_id
                if len(largest_id_v) > k:
                    min_key = min(largest_id_v, key=lambda x: largest_id_v[x])
                    largest_id_v.pop(min_key)
                    largest_id_t.pop(min_key)
        
        # count keys
        cnt = {}
        for k in largest_id_t.values():
            if k not in cnt:
                cnt[k] = 1
            else:
                cnt[k] += 1
        largest_type = max(cnt, key=lambda x: cnt[x])
        res = -1
        for tmpl_id in largest_id_t:
            if largest_id_t[tmpl_id] == largest_type:
                if res == -1:
                    res = tmpl_id
                else:
                    res = tmpl_id if largest_id_v[tmpl_id] < largest_id_v[res] else res

        return res
