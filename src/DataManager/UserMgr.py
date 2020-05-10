from DataManager.DataBase import db
import hashlib

class UserType:
    STUDENT = 0
    TEACHER = 1
    UNKNOWN = 2

class InfoFields:
    s_info = ('name', 'sid', 'tid')
    t_info = ('name', 'tid')


class UserMgr:
    def __init__(self):
        # self.user_type = user_type
        self.user_info = UserType.UNKNOWN
        self.logined = False

    def login(self, user_type, user_id: str, pwd: str):
        self.user_type = user_type
        pwd_cr = hashlib.sha256(pwd.encode()).hexdigest()
        table, id_type = ('Student', 'sid') \
            if self.is_student() else ('Teacher', 'tid')
        p = db.select(
            fields=('password',),
            table=table,
            condition='{}={}'.format(id_type, user_id)
        )
        p = p[0]['password']
        print(p)
        if p == pwd_cr:
            fields = InfoFields.s_info if self.is_student() \
                else InfoFields.t_info
            self.user_info = db.select(
                fields=fields, table=table,
                condition='{}={}'.format(id_type, user_id)
            )[0]
            self.logined = True
            return 0
        else:
            return -1

    def is_student(self):
        return self.user_type == UserType.STUDENT

    def login_status(self):
        return self.logined

    def get_name(self):
        return self.user_info['name']
    
    def get_id(self):
        return self.user_info['sid'] if self.is_student( )\
            else self.user_info['tid']


usermgr = UserMgr()