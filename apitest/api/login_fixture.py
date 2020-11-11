#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import AppxLogin, AppxLogout


def get_user_access_token(phoneNumber, password):
    '''
    获取访问令牌
    :param fn:
    :return:
    '''
    appid, token = _get_user_token(phoneNumber, password)

    # given
    url = AppxLogin.urls[1]
    method = AppxLogin.methods[1]
    headers = AppxLogin.headers[1]

    headers.update({
        "appid": appid,
        "Authorization": token

    })

    params = {
        "appId": appid
    }
    res = ConfigHttp(method=method, params=params, url=url, headers=headers).request().json()

    return res["data"]["token"]




def _get_user_token(phoneNumber, password):
    '''
    获得用户token
    :return:
    '''
    url = AppxLogin.urls[0]
    method = AppxLogin.methods[0]
    headers = AppxLogin.headers[0]
    data = AppxLogin.datas[0]

    data.update(
        {
            "password": password,
            "phoneNumber": phoneNumber

        }

    )
    res = ConfigHttp(method=method, url=url, data=data, headers=headers).request().json()
    appid = res["data"]["apps"][0]["appId"]
    token = res["data"]["token"]
    return appid, token


def appx_logout(token):
    url = AppxLogout.urls[0]
    method = AppxLogout.methods[0]
    headers = AppxLogout.headers[0]
    headers.update({
        "Authorization": token
    })
    res = ConfigHttp(method=method, url=url, headers=headers).request().json()

    MyLog.get_log().debug("退出 响应 ====" , res)






