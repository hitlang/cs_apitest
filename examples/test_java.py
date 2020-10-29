#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import jpype

jpype.startJVM("-Djava.class.path=test.jar")

date_class = jpype.JClass('java.util.Date')

# 实例化java对象
date_instance = date_class()

#静态方法不实例化
timestamp = date_instance.getTime()

print(timestamp)

#关闭虚拟机
jpype.shutdownJVM()