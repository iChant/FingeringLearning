import os
from PySide2.QtSql import QSqlQuery, QSqlDatabase

class DataBase:
    def __init__(self):
        db_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'data.db')
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(db_path)
        self.db.open()
        self.query = QSqlQuery()

    def select(self, fields: tuple, table: str, condition=None):
        """
        select items from table
        
        For example, to execute the sql state 
        `select name from Teacher where tid=1`,
        use `select(fields=('name',),
        table='Teacher', condition='tid=1')`

        params
        fields: tuple of str, such as ('id', 'name', 'type')
        table: str, name of target table
        condition: str, such as 'id=1'

        returns a list of dict
        """
        state = 'select {fields} from {table}'.format(
            fields=', '.join(fields),
            table=table
        )
        if condition is not None:
            state += ' where {con}'.format(con=condition)
        res = []
        self.query.clear()
        self.query.exec_(state)
        print(state)
        while self.query.next():
            item = {f: self.query.value(f) for f in fields}
            res.append(item)
        return res

    def insert(self, table: str, kv: dict):
        state = 'insert into {t} ({f}) values ({v})'.format(
            t=table,
            f=', '.join(kv.keys()),
            v=', '.join(kv.values())
        )
        print(state)
        return self.query.exec_(state)
    
    def __add_quote(self, s: str):
        return '"{}"'.format(s)


# For global singleton
db = DataBase()