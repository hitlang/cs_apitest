#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

#funA 作为装饰器函数
def funA(fn):
    #...
    fn() # 执行传入的fn参数
    #...
    return "A----"

@funA
def funB():
    print("B----")

if __name__ == '__main__':

    print(funB)

    pass