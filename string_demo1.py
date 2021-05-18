# -*-coding:utf-8-*-
from string import Template
from math import pi
from math import e
import math
if __name__ == "__main__":
    format = "Hello, %s. %s enough for ya?"
    values = ('world', 'Hot')
    print(format %values)

    tmpl = Template("Hello, $who! $what enough for ya?")
    print(tmpl.substitute(who = 'Mars', what = 'Dusty'))

    print("{}, {} and {}".format("first", "second", "third"))
    print("{0}, {1} and {2}".format("first", "second", "third"))
    print("{1} {0} {2} {3} {1} {0}".format("be", "to", "or", "not"))

    print("{name} is approximtely {values:.2f}.".format(name = "π", values = pi))

    print(f"Euler's constant is roughly {e}.")
    print("Euler's constant is roughly {e}.".format(e = e))

    fullname = ["Alfred", "Smoketoomuch"]
    print("Mr {name[1]}".format(name = fullname))

    #替换字段名
    tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
    print(tmpl.format(mod=math))

    #基本转换
    print("{pi!s} {pi!r} {pi!a}".format(pi = "π"))

    print("The number is {num}".format(num = 12))
    print("The number is {num:f}".format(num = 12))
    print("The number is {num:b}".format(num = 12))

    #宽度、精度和千位分隔符
    print("{num:10}".format(num = 3))
    print("{name:10}".format(name = "Bob"))
    print("pi day is {pi:.2f}".format(pi = pi))
    print("{pi:10.2f}".format(pi = pi))
    print("{:.5}".format("Guido van Russum"))
    print("One googol is {:,}".format(10**100))

    #符号、对齐和0填充
    print("{:010.2f}".format(pi))
    print("{0:<10.2f}\n {0:^10.2f}\n {0:>10.2f}".format(pi))
    print("{:$^20}".format("WIN BIG"))

    print("{0:10.2f}\n {1:10.2f}".format(pi,-pi))

    #根据指定的宽度打印格式良好的价格列表
    width = int(input("Please enter width:"))

    price_width = 10
    item_width = width - price_width

    header_fmt = "{{:{}}} {{:>{}}}".format(item_width, price_width)
    fmt        = "{{:{}}} {{:>{}.2f}}".format(item_width, price_width)

    print('=' * width)
    print(header_fmt.format("Irem", "price"))
    print('-' * width)
    print(fmt.format("Apples", 0.4))
    print(fmt.format("Pears", 0.5))
    print(fmt.format("Cantaloupes", 1.92))
    print(fmt.format("Bananes", 8))
    print(fmt.format("Origin", 1.5))
    print('-' * width)

    #字符串方法
    # string.digits：包含数字0～9的字符串。
    # string.ascii_letters：包含所有ASCII字母（大写和小写）的字符串。
    # string.ascii_lowercase：包含所有小写ASCII字母的字符串。
    # string.printable：包含所有可打印的ASCII字符的字符串。
    # string.punctuation：包含所有ASCII标点字符的字符串。
    # string.ascii_uppercase：包含所有大写ASCII字母的字符串

    # 方法center通过在两边添加填充字符（默认为空格）让字符串居中
    print( "The Middle by Jimmy Eat World".center(39))
    print( "The Middle by Jimmy Eat World".center(39, "*"))

    # 方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回 - 1
    # 字符串方法find返回的并非布尔值。如果find像这样返回0，就意味着它在索引0处找到了指定的子串
    print('With a moo-moo here, and a moo-moo there'.find('moo'))
    print("Monty Python's Flying Circus".find("Monty"))
    print("Monty Python's Flying Circus".find("M"))
    print("Monty Python's Flying Circus".find("Tom"))

    # join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素。
    # print("+".join([1, 2, 3, 4, 5]))
    print("+".join(['1', '2', '3', '4', '5']))
    print('/'.join(['', 'usr', 'bin', 'env']))
    print("C" + "\\".join(('', 'usr', 'bin', 'env')))









































