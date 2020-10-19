#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import jpype

jpype.startJVM()

jpype.java.lang.System.out.println("hello world!")

jpype.shutdownJVM()