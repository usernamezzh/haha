# -*-coding:utf-8-*-

import sys

# 模块（模块是一个包含所有你定义的函数和变量的文件，其后缀名为.py。模块可以被别的程序引入，以使用模块中的函数等功能）

print("命令行参数如下：")
for i in sys.argv:
    print(i)

print("python路径为：", sys.path)

# import语句
# 想使用python源文件，只需在另一个源文件里执行import语句，语法import module1[,module2[,...moduleN]
# 当解释器遇到import语句，如果模块在当前搜索路径就会被导入。

def print_func(par):
    print("hello", par)
    return

# 一个模块只会被导入一次，不管你执行了多少次import.这样可以防止被导入的模块一遍又一遍的执行。

def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    print(result)
    return result
