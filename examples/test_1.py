#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

from  collections import defaultdict

x = defaultdict(list)


x["a"].append(2)
x["a"].append(3)
x["a"].append(4)

print(dict(x))

