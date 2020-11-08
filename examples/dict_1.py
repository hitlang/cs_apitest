#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
多值映射字典
'''
d = {}



d.setdefault("a" , []).append("1")

d.setdefault("a", []).append("2") # 别扭，每次创建一个空列表

print(d)