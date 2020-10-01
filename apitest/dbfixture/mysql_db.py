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

    # clear table data
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
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
            cursor.execute(real_sql)

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
    db = DB()
    now = round(time())
    table_name = "dbshop_user"

    test_data = {
        "group_id": 1,
        "user_name": "test7",
        "user_password": "4f8b6e3cc0dbe66cb0ba5c9d41c0a80d",
        "user_email": "test7@dt.com",
        "user_sex": 3,
        "user_time": now,
        "user_state": 1,
        "user_integral_num": 0,
        "integral_type_2_num": 0,
        "user_money": 0.00
    }

    db.insert(table_name, test_data)
    db.close()

    pass
