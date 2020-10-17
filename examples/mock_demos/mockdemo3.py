#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

from unittest.mock import  Mock



m = Mock(return_value = "1" ,side_effect=[2 , 3, 4])


print(m())
print(m())
print(m())







