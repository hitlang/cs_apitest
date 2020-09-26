#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
"""
封装各种加密方法

"""
import hashlib
#dbshop 数据库加密md5 盐值
SALT = b'?3b)f*ixoY!WQ4t{jyk#<{/HZXIw$>7Kr?+VN`?tN8qRJZ?6GW|oJW|{z+KBe2@?'
def md5(pwd):
    # 实例化对象
    obj = hashlib.md5(SALT)
    # 写入要加密的字节
    obj.update(pwd.encode('utf-8'))
    # 获取密文
    return obj.hexdigest()

if __name__ == '__main__':
    print(md5("123456"))
    pass