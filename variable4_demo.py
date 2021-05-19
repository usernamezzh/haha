# -*-coding:utf-8-*-
# 全局变量：
# 全局变量是在函数外部定义的变量，所有函数内部都可以使用这个变量

num = 10
def demo1():
    print(num)

def demo2():
    print(num)

# 1.函数不能直接修改全局变量的引用
# 全局变量是在函数外部定义的变量（没有定义在某个函数内），所有函数内部都可以使用这个变量
# 在函数内部，可以通过全局变量的引用获取对应的数据，但是不允许直接修改全局变量的引用--使用赋值语句修改全局变量的值
# 注意：只是在函数内部定义了一个局部变量而已，只是变量名相同--在函数内部不能直接修改全局变量的值
#如果在函数中需要修改全局变量，需要使用global进行申明
def demo3():
    print("demo3" + "-" * 50)
    num = 100
    print(num)

def demo4():
    print("demo4" + "-" * 50)
    print(num)

def demo5():
    print("demo5" + "-" * 50)
    global num
    num = 100
    print(num)

def demo6():
    print("demo6" + "-" * 50)
    print(num)

if __name__ == "__main__":
    demo1()
    demo2()
    demo3()
    demo4()
    demo5()
    demo6()
    print("over")