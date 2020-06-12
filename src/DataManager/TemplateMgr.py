from .DataBase import db
from .UserMgr import usermgr
from config import ROOT_PATH

from PySide2.QtSql import QSqlRelationalTableModel, QSqlRelation
from PySide2.QtCore import Qt

import numpy as np
import os
import time

class TypeInfo:
    def __init__(self):
        type_list = db.select(fields=('type_name', 'type_id'), table='TypeInfo')
        self.id_name = {int(i['type_id']): i['type_name'] for i in type_list}
        self.name_id = {i['type_name']: int(i['type_id']) for i in type_list}

    def get_name_by_id(self, type_id):
        return self.id_name[int(type_id)]

    def get_id_by_name(self, type_name):
        return self.name_id[type_name]
    
    def get_name_list(self):
        return list(self.id_name.values())


type_info = TypeInfo()


class TemplateMgr:
    def __init__(self):
        pass

    def add_record(self, type_id, filepath, tid):
        # if not usermgr.login_status():
        #     return -1
        res = db.insert(table='Template', 
            kv={'type_id': str(type_id),
                'filepath': '"{}"'.format(filepath),
                'tid': str(tid)})
        return res

    def get(self, **kargs):
        """
        Return a list of template file paths which fit
        the given conditions specified in `kargs`. If
        no params passed, the method will return the
        whole list recorded in the database.

        :param id: item with specific id
        :param type_id: items with specific type_id
        :param type_name: items with specific type_name

        :return: a dict contains the list of results
        """
        if len(kargs) == 0:
            l = db.select(fields=('id', 'filepath', 'type_id'), table='Template')
        else:
            conds = ['{}={}'.format(k, str(kargs[k])) for k in kargs]
            condition = ' AND '.join(conds)
            l = db.select(fields=('id', 'filepath', 'type_id'),
                table='Template', condition=condition)
        res = {}
        for i in l:
            if i['type_id'] not in res:
                res[i['type_id']] = []
            res[i['type_id']].append((i['id'], i['filepath']))
        # print(res)
        return res

    def save_tmpl(self, data, type_name):
        cnt = len(self.get(type_name=type_name))
        filename = '{}.npy'.format(int(time.time()))
        path = os.path.join(ROOT_PATH, 'Template', filename)
        # print(path)
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        np.save(path, data)
        res = self.add_record(
            type_info.get_id_by_name(type_name), path, usermgr.get_id())
        if not res:
            print(db.query.lastError())

    def read_data(self, tmpl_id):
        filepath = list(self.get(id=tmpl_id).values())[0][0][1]
        return np.load(filepath)

    def get_type_id(self, tmpl_id):
        tmpl_id = db.select(
            fields=('type_id',), table='Template', condition='id={}'.format(str(tmpl_id)))
        return int(tmpl_id[0]['type_id'])

    def remove_data(self, tmpl_id):
        filepath = list(self.get(id=tmpl_id).values())[0][0][1]
        if os.path.exists(filepath):
            os.remove(filepath)

tmplmgr = TemplateMgr()


class TmplModel:
    def __init__(self, parent=None):
        # dirpath = os.path.dirname(os.path.abspath(__file__))
        # self.db = QSqlDatabase.addDatabase('QSQLITE')
        # self.db.setDatabaseName(os.path.join(dirpath, 'grad.db'))
        # self.db.open()
        self.model = QSqlRelationalTableModel(parent)
        self.model.setTable('Template')
        self.model.setRelation(3, QSqlRelation('Teacher', 'tid', 'name'))
        self.model.setHeaderData(3, Qt.Horizontal, 'teacher')
        self.model.setRelation(4, QSqlRelation('TypeInfo', 'type_id', 'type_name'))
        self.model.setHeaderData(4, Qt.Horizontal, 'type')
        self.model.select()
    
    def refresh(self):
        self.model.select()
