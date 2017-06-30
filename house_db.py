import sqlite3

class House_db(object):
    def __init__(self):
        self.db = None

    def connect(self):
        try:
            self.db = sqlite3.connect("house.db")
            sql_create_table = """create table if not exists 'house_info' (
            'id' INTEGER PRIMARY KEY,
            'info' STRING
            """
if
house_table = Table('house', metadata, Column('id', Integer, primary_key=True),
                    Column('house_info', String(256)),
                    Column('zongjia', String(24)),
                    Column('danjia', String(24)),
                    Column('huxing', String(24)),
                    Column('mianji', String(24)),
                    Column('zhuangxiu', String(24)),
                    Column('leibie', String(24)),
                    Column('louceng', String(24)),
                    Column('chaoxiang', String(24)),
                    Column('niandai', String(24)),
                    Column('dizhi', String(128)))

house_table.create()
