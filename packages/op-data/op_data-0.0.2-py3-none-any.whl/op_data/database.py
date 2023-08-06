import sqlalchemy
import pandas as pd
import cx_Oracle
from urllib import parse


class Mysql:
    def __init__(self, username, password, connect):
        conn_str = 'mysql+pymysql://{0}:{1}@{2}'.format(username, parse.quote_plus(password), connect)
        print(conn_str)
        self.conn = sqlalchemy.create_engine(conn_str)

    def sql(self, sql):
        data = pd.read_sql(sql, self.conn)
        print(data)
        return data

    def close(self):
        self.conn.dispose()


class Oracle:
    def __init__(self, username, password, connect):
        self.conn = cx_Oracle.connect(username, password, connect)
        print('oracle 版本：' + self.conn.version)
        self.c = self.conn.cursor()

    def sql(self, sql):
        data = self.c.execute(sql).fetchall()
        print(data)
        return data

    def close(self):
        self.c.close()
        self.conn.close()
