#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

from unittest.mock import  Mock



# m = Mock(return_value = "1" ,side_effect=Exception("abc"))
m = Mock(return_value = "1" )

x = m()

# print(m.called) #是否被调用
# print(m.call_count) # 调用次数







