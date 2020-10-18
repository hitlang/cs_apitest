#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

class Student:
    def __init__(self, name) -> None:
        self.name = name

    def info(self):
        print(self.name)

    def __call__(self, *args):
        print(args)

        print("ddddddddddddddddddddddddddddddddddddddddddddddddddd")


def add():

    print("add")


if __name__ == '__main__':

    s = Student("kevin")
    # #
    s.info()

    s()

