#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang


def  get_orderPayFinish(configHttp):
    '''
    发送订单完成支付请求
    :return:
    '''
    res = configHttp.request().json()
    return res

