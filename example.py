# -*-coding:utf8-*-

import cmath
import math
import random

def fun1():
    print("Hello world!")
    return

def fun2(a,b):
    sum = a + b
    print(sum)
    return sum

def fun3():
    while 1:
        x = input("请输入数字x的值：")
        y = input("请输入数字y的值：")
        try:
            sum = (float(x) + float(y))
        except:
            print("输入的数字格式不正确，请重新输入")
            continue
        else:
            print("数字{0}和数字{1}的和为{2}".format(x,y,sum))
            break
    return sum

def fun4():
    x = input("请输入数字x的值：")
    y = input("请输入数字y的值：")
    sum = float(x) + float(y)
    print("数字{0}和数字{1}的和为{2}".format(x,y,sum))
    return sum

# 我们通过用户输入一个数字，并使用指数运算符**来计算该数的平方根，该程序只适用于正数
def fun5():
    x = float(input("请输入数字x:"))
    x_sqrt = x ** (1/2)
    print("%0.3f的平方根等于%0.3f"%(x,x_sqrt))
    return x_sqrt

# 使用cmath(comples math)模块的sqrt方法来计算负数和复数的平方根。
def fun6():
    x = float(input("请输入数字x:"))
    x_sqrt = cmath.sqrt(x)
    print("{0}的平方根等于{1}".format(x,x_sqrt))
    return x_sqrt

def fun7():
    a = float(input("输入a:"))
    b = float(input("输入b:"))
    c = float(input("输入c:"))
    d = b*b - 4*a*c
    sol1 = (-b + cmath.sqrt(d))/(2*a)
    sol2 = (b +cmath.sqrt(d))/(2*a)
    print("二次方程的两个解为{0}和{1}".format(sol1,sol2))
    return sol1,sol2

def fun8():
    a = float(input("输入三角形第一边长："))
    b = float(input("输入三角形第二边长："))
    c = float(input("输入三角形第三边长："))
    s = (a + b + c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print("三角形面积为%0.2f"%area)

def fun9(r):
    s = math.pi*(r*r)
    print("圆的面积等于：",s)

def fun10():
    print(random.randint(0,9))
# 函数返回数字N，N为a到b之间的数字（a >= N >= b）,包含a和b

def fun11():
    celsius = float(input("输入摄氏温度："))
    fahrenheit = celsius * 1.8 + 32
    print("%0.1f摄氏温度的华氏温度为%0.1f"%(celsius,fahrenheit))

def fun12(x,y):
    temp = x
    x = y
    y = temp
    print("交换后x的值为：{}".format(x))
    print("交换后y的值为：{}".format(y))

def fun13():
    x = input("请输入x的值为：")
    y = input("请输入y的值为：")
    x,y = y,x
    print("交换后x的值为：{}".format(x))
    print("交换后y的值为：{}".format(y))

def fun14(num):
    if num > 0:
        print("{}是正数".format(num))
    elif num == 0:
        print("{}是零".format(num))
    else:
        print("{}是负数".format(num))

def fun15():
    num = float(input("请输入一个数字："))
    if num >= 0:
        if num > 0:
            print("{}是正数".format(num))
        else:
            print("{}是零".format(num))
    else:
        print("{}是负数".format(num))

def fun16():
    while True:
        try:
            num = float(input("请输入一个数字："))
            if num > 0:
                print("{}是正数".format(num))
            elif num == 0:
                print("{}是零".format(num))
            else:
                print("{}是负数".format(num))
            break
        except ValueError:
            print("输入无效，需要输入一个数字")
            continue

def fun17(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass

    return False

# print(fun17('foo'))
# print(fun17('5'))
# print(fun17('1.5'))

if __name__ == "__main__":
    fun1()
    fun2(10,20)
    fun3()
    fun4()
    fun5()
    fun6()
    fun7()
    fun8()
    fun9(2)
    fun10()
    fun11()
    fun12(1,2)
    fun13()
    fun14(5)
    fun15()
    fun16()
    print(fun17('foo'))
    print(fun17('5'))
    print(fun17('1.5'))