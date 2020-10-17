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

#
#
# m = Mock(spec = ["name" , "age"]) #属性列表
#
#
# print(m.name)
# print(m.age)



m2 = Mock(spec= Student)

print(m2.info)
print(m2._gender)




