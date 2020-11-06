# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import pymysql.cursors
from time import time
# ======== Reading db_config.ini setting ===========
# from config import Config
#
# cf = Config()
from config import global_config

cf = global_config
host = cf.getMysqlConf("host")
port = cf.getMysqlConf("port")
db = cf.getMysqlConf("db_name")
user = cf.getMysqlConf("user")
password = cf.getMysqlConf("password")
# ======== MySql base operating ===================
class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              database=db,
                                              charset='utf8',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def delete(self,sql, values):
        with self.connection.cursor() as cursor:
            r = cursor.execute(sql, values)
        self.connection.commit()
        return r


    # clear table data
    def clear(self, table_name , user_name ):
        '''

        :param table_name:
        :param values:  ("user_name" : "test111")
        :return:
        '''
        real_sql = "delete from " + table_name + " where " + "user_name = %s;"

        with self.connection.cursor() as cursor:
            r =  cursor.execute(real_sql, (user_name,))
            print("delete ", r)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        # print(real_sql)

        with self.connection.cursor() as cursor:
            r = cursor.execute(real_sql)
        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':

    sql = "delete from dbshop_user where user_name = %s "

    values = ("xionglin",)
    db = DB()

    r = db.delete(sql, values)

    print(r)


    pass
