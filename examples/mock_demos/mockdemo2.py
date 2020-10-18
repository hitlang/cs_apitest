#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

from unittest.mock import  Mock
#调用抛出异常
m = Mock(return_value = "1" ,side_effect = Exception("异常"))
print(m())








