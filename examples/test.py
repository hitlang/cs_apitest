#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
全局变量注意事项
'''
class Stu():

    def __init__(self, name) -> None:
        print("call ...........")
        self.name = name

        pass

    def getName(self):

        return self.name

def foo1():
    global  stu
    stu =Stu("kevin")

    print(stu.getName())
    pass


def foo2():
    global stu


    print(stu.getName())
    pass

foo1()

foo2()