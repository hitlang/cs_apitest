#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import requests
from unittest import mock

def request_baidu():
    resp = requests.get('http://www.baidu.com')
    return resp.status_code

# 模拟调用request_baidu，且返回值是500
request_baidu = mock.Mock(return_value=500)
print(request_baidu())
