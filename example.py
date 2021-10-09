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

def fun18(num):
    if num % 2 == 0:
        print("该数是偶数")
    else:
        print("该数是奇数")

def fun19(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("该年是闰年")
            else:
                print("该年是平年")
        else:
            print("该年是闰年")
    else:
        print("该年是平年")

def fun20():
    year = int(input("请输入年份："))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("{}年是闰年".format(year))
    else:
        print("{}年是平年".format(year))
    return

def fun21():
    print(max(1,2))
    print(max('a','b'))
    print(max([1,2]))
    print(max((1,2)))
    print("10, 20, -10中最大值为：",max(10,20,-10))
    print("-50, 100, 200中最大值为：",max(-50,100,200))
    print("200, -200, 100中最大值为：",max(200,-200,100))

def fun22():
    num = int(input("请输入一个数字："))
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print("{}不是质数".format(num))
                print("{}乘于{}是{}".format(i,num // i,num))
                break
        else:
            print("{}是质数".format(num))
    else:
        print("{}不是质数".format(num))

def fun23():
    while 1:
        try:
            num = int(input("请输入一个数："))
            if num == 2:
                print("质数")
            else:
                if num == 0 or num == 1:
                    print("都不是")
                else:
                    u = num - 2
                    h = 1
                    p = 1
                    while u:
                        h = h + 1
                        if num % h == 0:
                            p = 1
                            break
                        else:
                            p = 0
                        u = u - 1
                    if p:
                        print("合数")
                        break
                    else:
                        print("质数")
                        break
        except ValueError:
            print("输入的内容不对，请重新输入。")

def fun24():
    upper = int(input("请输入区间最大值："))
    lower = int(input("请输入区间最小值："))
    for num in range(lower,upper+1):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                print(num)

def fun25(num):
    print(math.factorial(num))

def fun26():
    num = 1
    x = int(input("请输入x的值："))
    for i in range(1,x + 1):
        num *= i
    print("{}的阶乘等于{}".format(x,num))

# def fun27():
# #     num = int(input("请输入一个数字："))
# #     if num < 0:
# #         print("该数没有阶乘。")
# #     elif num == 0:
# #         print("0的阶乘等于1。")
# #     else:
# #         return num * fun27(num -

def fun28():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d * %d = %d\t"%(j,i,i*j), end = '')
        print()

def fun29():
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            print("{} * {} = {}\t".format(j, i, i*j),end = '')
            j += 1
        print()
        i += 1

def fun30():
    for i in range(1,10):
        j = 1
        while j <= i:
            print("{} * {} = {}\t".format(j, i, j*i),end = '')
            j += 1
        print()

def fun31():
    i = 1
    while i < 10:
        for j in range(1,i+1):
            print("%d * %d = %2d\t"%(j, i, j*i),end = '')
        print()
        i += 1

def fun32():
    a = [1,2,3,4,5,6,7,8,9]
    for i in a:
        j = 1
        while j <= i:
            print("{} * {} = {}\t".format(j, i, i*j),end = '')
            j += 1
        print()

def fun33():
    for i in range(1,10):
        for j in range(1,10-i):
            print(end='           ')
        for k in  range(1,i+1):
            print("%d * %d = %2d"%(k,i,k*i),end=' ')
        print("")

def fun34():
    nterms = int(input("您需要几项？"))
    n1 = 0
    n2 = 1
    count = 2

    if nterms <= 0:
        print("请输入一个正整数。")
    elif nterms == 1:
        print("斐波那契数列：")
        print(n1)
    else:
        print("斐波那契数列：")
        print(n1,',',n2,end = ',')
        while count < nterms:
            nth = n1 + n2
            print(nth, end = ',')
            n1 = n2
            n2 = nth
            count += 1



if __name__ == "__main__":    # fun1()
    # fun2(10,20)
    # fun3()
    # fun4()
    # fun5()
    # fun6()
    # fun7()
    # fun8()
    # fun9(2)
    # fun10()
    # fun11()
    # fun12(1,2)
    # fun13()
    # fun14(5)
    # fun15()
    # fun16()
    # print(fun17('foo'))
    # print(fun17('5'))
    # print(fun17('1.5'))
    # fun18(10)
    # fun19(1900)
    # fun20()
    # fun21()
    # fun22()
    # fun23()
    # fun24()
    # fun25(3)
    # fun26()
    # fun27()
    fun28()
    fun29()
    fun30()
    fun31()
    fun32()
    fun33()
    fun34()