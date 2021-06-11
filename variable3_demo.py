# -*- coding:utf-8-*-
# 局部变量
# 1.局部变量：
# 局部变量是在函数内部定义的变量，只能自函数内部使用
# 函数执行结束后，函数内部的局部变量会被系统回收
# 不同的函数，可以定义相同名称的局部变量，但是彼此之间不会产生影响
# 2.局部变量的生命周期
# 所谓生命周期就是变量被创建到被系统回收的过程
# 局部变量在函数执行时才会被创建
# 函数执行结束后局部变量被系统回收
# 局部变量在生命周期内，可以用来存储函数内部临时使用到的数据
#注意：函数执行时，需要处理变量时会首先查找函数内部是否存在指定名称的全局变量，如果有直接使用。如果没有，查找函数外部是否存在指定名称的全局变量，如果有直接使用，如果没有报错。
def demo1():
    num = 10
    print(num)
    print("数据创建时的内存地址%d"%id(num))
    num = 20
    print(num)
    print("数据修改后的内存地址%d"%id(num))

def demo2():
    num = 100
    print(num)

if __name__ == "__main__":
    demo1()
    demo2()
    print("over")