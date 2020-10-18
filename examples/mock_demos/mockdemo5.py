#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

from unittest.mock import  Mock
class Student():

    _gender = None

    def __init__(self, name) -> None:
        self.name = name


    def info(self, x ):
        return self.name + x

if __name__ == '__main__':

    m = Mock(spec = Student)

    s = Student("kevin")

    print(m.info(1))

    m.info.assert_called_with(1)

    pass