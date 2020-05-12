from .DataBase import db
# from .UserMgr import usermgr
# from config import ROOT_PATH

from PySide2.QtSql import QSqlRelationalTableModel, QSqlRelation
from PySide2.QtCore import Qt

class ScoreMgr:
    def __init__(self):
        pass

    def add(self, data, sid, type_id):
        return db.insert(table='Score', 
            kv={'global_score': str(data['total']),
                'thumb_score': str(data['thumb']),
                'index_score': str(data['index']),
                'middle_score': str(data['middle']),
                'ring_score': str(data['ring']),
                'pinky_score': str(data['pinky']),
                'sid': str(sid),
                'type_id': str(type_id)})
    
    def last_error(self):
        return db.last_error().text()

scoremgr = ScoreMgr()

class ScoreModel:
    def __init__(self, fil: str = None, parent=None):
        self.model = QSqlRelationalTableModel(parent)
        self.model.setTable('Score')
        self.model.setRelation(9, QSqlRelation('TypeInfo', 'type_id', 'type_name'))
        self.model.setHeaderData(9, Qt.Horizontal, 'type')
        if fil is not None:
            self.model.setFilter(fil)
        self.model.select()
        print(self.model)
