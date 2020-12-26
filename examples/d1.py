#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
 求笛卡尔积
'''

import itertools
test_data = [1,2,3]
data1 = [ 4, 5 ,6]
data2 = [ 7, 8, 9 , 10 ]

data = [test_data ,data1, data2]


for item in itertools.product(*data):
    print(item)

