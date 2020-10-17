#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

from unittest.mock import  Mock

class Student():


    def __init__(self, name) -> None:
        self.name = name


    def info(self, x ):
        return self.name + x



m = Mock(name="m1" , return_value = Student("kevin"))

x = m()

print(x.info("y"))






