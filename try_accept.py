# -*-coding:utf-8-*-

import sys

# python有两种错误很容易辨认：语法错误和异常。
# python assert(断言)用于判断一个表达式，在表达式条件为false的时候触发异常。
#           try：
#                         执行代码
#           except：
#                         发生异常时执行的代码


# 异常处理（try/except）
while True:
    try:
        x = int(input("请输入一个数字："))
        break
    except ValueError:
        print("您输入的不是一个数字，请尝试再次输入！")

# try语句按照如下方式执行：
# 首先执行try子句（在关键字try和except之间的语句）。
# 如果没有异常发生，忽略except子句，try子句执行后结束。
# 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和except之后的名称相符，那么对应的except子句将被执行。
# 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。


# 一个try语句可能包含多个except子句，分别来处理不同的异常。最多只有一个分支会被执行。
# 处理程序将只针对对应try子句中的异常进行处理，而不是其它try的处理程序中的异常。
# 一个except语句可以同时处理多个异常，这些异常将会被放在一个括号里成为一个元组，例如：
# except(RuntimeError,TypeError,NameError):
#     pass
# 最后一个except子句可以忽略异常的名称，它将被当做通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

try:
    f = open(r"C:\Users\Administrator\Desktop\test.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# try/except...else
# try/except语句还有一个可选的else子句，那么必须放在所有的except子句之后。else子句将在try子句没有发生任何异常的时候执行。
#         try
#                     执行代码
#         except
#                     发生异常时执行的代码
#         else
#                     没有异常时执行的代码
for arg in sys.argv[1:]:
    try:
        f = open(arg, "r")
    except IOError:
        print("cannot", arg)
    else:
        print(arg,'has',len(f.readline()),"lines")
        f.close()
# 使用else子句比把所有的语句都放在try子句里面要好，这样可以避免一些异想不到，而except又无法捕获的异常。
# 异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常.

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print("handling run-time error:",err)


# try-finally语句：try-finally语句无论是否发生异常，都将执行最后的代码。
#         try
#                     执行代码
#         except
#                     发生异常时执行的代码
#         else
#                     没有发生异常时执行的代码
#         finally
#                     不管有没有异常都会被执行的代码

def runoob():
    print("Hello Runoob!")
try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open(r'C:\Users\Administrator\Desktop\test.txt') as file:
            read_data = file.read()
            print(read_data)
    except FileNotFoundError as err:
        print(err)
finally:
    print("无论异常是否发生都会执行。")

# 抛出异常 python使用raise抛出一个指定的异常
# x = 10
# if x > 5:
#     raise Exception('x不能大于5，x的值为：{}'.format(x))
# raise唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是一个异常的类（也就是Exception的子类）。
try:
    raise NameError('Hithere')
except NameError:
    print('An exception flew by')
    raise

# 用户自定义异常
# 可以创建一个新的异常类来拥有自己的异常。异常类继承自Exception类，可以直接继承，或者间接继承。
