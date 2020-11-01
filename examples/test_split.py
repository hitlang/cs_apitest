#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang


cookie = "PHPSESSID=d9643h35fcjugc536rsekha8p0"

list1 = cookie.split("=")

r = [ value  for  value in list1]

print(r)
# cookie = {key: value for key, value in cookie.split("=")}
#
# print(cookie)