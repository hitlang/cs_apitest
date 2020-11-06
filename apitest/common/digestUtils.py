# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
"""
封装各种加密方法

"""
import binascii
import hashlib

# dbshop 数据库加密md5 盐值
SALT = b'?3b)f*ixoY!WQ4t{jyk#<{/HZXIw$>7Kr?+VN`?tN8qRJZ?6GW|oJW|{z+KBe2@?'


def md5(pwd):
    # 实例化对象
    obj = hashlib.md5(SALT)
    # 写入要加密的字节
    obj.update(pwd.encode('utf-8'))
    # 获取密文
    return obj.hexdigest()


def my_md5(msg):
    """
    md5 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    obj = hashlib.md5()
    # 写入要加密的字节
    obj.update(msg.encode('utf-8'))
    # 获取密文
    return obj.hexdigest()


def my_sha1(msg):
    """
    sha1 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    sh = hashlib.sha1()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()




if __name__ == '__main__':
    # print(md5("123456"))
    print(my_md5("123456"))
    pass
