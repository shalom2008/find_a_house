import sqlite3


class HouseDB(object):
    def __init__(self):
        self.db = None

    def connect(self):
        try:
            self.db = sqlite3.connect("house.db")
            sql_create_table = """create table if not exists `house_info` (
            `id` INTEGER,
            `info` CHAR(512),
            `zongjia` CHAR(48),
            `danjia` CHAR(48),
            `huxing` CHAR(48),
            `mianji` CHAR (48),
            `zhuangxiu` CHAR (48),
            `leibie` CHAR (48),
            `louceng` CHAR (48),
            `chaoxiang` CHAR (48),
            `niandai` CHAR (48),
            `dizhi` CHAR (256),
            `url` CHAR (512))
            """
            self.db.execute(sql_create_table)
        except Exception as e:
            print('sqlite3 connect fail.' + str(e))

    def close(self):
        try:
            if self.db:
              self.db.close()
        except BaseException as e:
            print('sqlite3 close fail.' + str(e))

    def insert_table(self, dict_data=None):
        if not dict_data:
            return False
        try:
            cols = ','.join(dict_data.keys())
            values = ','.join(dict_data.values())
            sql_insert = 'insert into `house_info` (%s) values (%s)' % (cols, '"'+values+'"')
            self.db.execute(sql_insert)
            self.db.commit()
        except BaseException as e:
            self.db.rollback()
            print("sqlite3 insert fail." + str(e))
        return True

    def compare(self, id, zongjia):
        if not id or not zongjia:
            return False
        compare_sql = 'select count(*) from `house_info` WHERE id==%d and'\
                      ' zongjia==%s' % (id, '"'+zongjia+'"')
        cursor = self.db.execute(compare_sql)
        return cursor

    def find_house(self, zongjia):
        if not zongjia:
            return False
        result = list()
        find_sql = 'select * from `house_info` WHERE zongjia==%s' % ('"'+zongjia+'"')
        cursor = self.db.execute(find_sql)
        for row in cursor:
            result.append({'id':row(0),'info':row(1),'zongjia':row(2),'danjia':row(3),\
                           'huxing':row(4),'mianji':row(5),'zhuangxiu':row(6), \
                           'leibie':row(7),'louceng':row(8),'chaoxiang':row(9), \
                           'niandai':row(10),'dizhi':row(11),'url':row(12)})
        return result

    def drop_table(self):
        drop_sql = 'drop table `house_info`'
        cursor = self.db.execute(drop_sql)
        return cursor


if __name__ == '__main__':
    table = HouseDB()
    table.connect()
    table.drop_table()