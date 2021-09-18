# -*-coding:utf8-*-

import cmath
import math

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