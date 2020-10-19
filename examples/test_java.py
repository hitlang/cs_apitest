#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import jpype

jpype.startJVM("-Djava.class.path=test.jar")

javaclass = jpype.JClass('com.cs.Hello')

# 实例化java对象
# javaInstance = javaclass()

#静态方法不实例化
javaclass.getMsg()

#关闭虚拟机
jpype.shutdownJVM()