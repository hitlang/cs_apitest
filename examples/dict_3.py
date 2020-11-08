#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
多值映射字典  集合
'''

from collections  import  defaultdict

d = defaultdict(set) #对象

d["a"].add(1)
d["a"].add(2)
d["a"].add(3)

print(dict(d))


