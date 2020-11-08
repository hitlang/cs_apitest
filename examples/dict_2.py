#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
多值映射字典 列表
'''

from collections  import  defaultdict

d = defaultdict(list) #对象

d["a"].append(1)
d["a"].append(2)

d["b"].append(3)

print(d)


