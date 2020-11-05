#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import unittest
import  time
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import AppxClassAdd
from config import global_config


class TestClassificationAdd(unittest.TestCase):


    def setUp(self) -> None:
        self.aca = AppxClassAdd()
        self.log = MyLog.get_log()
        self.config = global_config
        pass

    def test_class_upload_file(self):
        '''
        上传分组图片
        :return:
        '''
        image = open(r"E:\cs_apitest\cs_apitest\apitest\data\test_03.jpg", "rb")
        url , data , headers , method  = self.aca.urls[0],self.aca.datas[0],self.aca.headers[0],self.aca.methods[0]

        headers.update({
            "Authorization": self.config.getToken()

        })
        files = {"file":image}
        #when
        res = ConfigHttp(method=method, url=url,  data=data, headers=headers, files=files).request().json()

        self.log.debug("upload_file  res ==={}".format(res))

        #then

        self.assertEqual(res["code"] , "000000")
        self.assertEqual(res["comment"] , "Completed successfully")
        #out

        image.close()

        global  img_url

        img_url = res["data"][0]

    def test_class_add_smoke(self):
        global  img_url
        '''
         增加分组
        :return: 
        '''


        url, data, headers, method = self.aca.urls[1], self.aca.datas[1], self.aca.headers[1], self.aca.methods[1]

        headers.update({
            "Authorization": self.config.getToken()

        })

        data.update({
            "name": "测试分类名" + str(round(time.time())),
            "logo": img_url
        })

        res = ConfigHttp(method=method, url=url,  data=data, headers=headers).request().json()

        self.log.debug("class add res ==={}".format(res))

        #then

        self.assertEqual(res["code"] , "000000")
        self.assertEqual(res["comment"] , "Completed successfully")
        pass



