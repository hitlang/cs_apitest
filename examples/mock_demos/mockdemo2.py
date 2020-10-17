#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

from unittest.mock import  Mock



m = Mock(return_value = "1" ,side_effect=Exception("abc"))

x = m()








