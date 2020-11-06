#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

def funA(fn):
    # 定义一个嵌套函数
    def say(*args,**kwargs):
        fn(*args,**kwargs)
    return say

@funA
def funB(arc):
    print("C语言中文网：",arc)

@funA
def other_funB(name,arc):
    print(name,arc)

funB("http://c.biancheng.net")

other_funB("Python教程：","http://c.biancheng.net/python")