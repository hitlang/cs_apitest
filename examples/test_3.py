#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("Python教程:",arc)
    return say

@funA
def funB(arc):
    print("funB():", arc)


funB("http://c.biancheng.net/python")