# -*-coding:utf-8-*-

import builtins

# 命名空间：命名空间是名称到对象的映射，大部分的命名空间都是通过字典来实现的。
# 命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。
# 我们举一个计算机系统中的例子，一个文件夹（目录）中可以包含多个文件夹，每个文件夹中不能有相同的文件名，但不同文件夹中的文件可以重名。

# 一般有三种命名空间：内置名称，全局名称，局部名称
# 内置名称（built-in names）：Python内置的名称，比如：abs,char和异常名称BaseException、Exception等。
# 全局名称 (global names)：模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 局部名称（local names）: 函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

# 命名空间查找顺序
# 加入我们要使用变量runoob,则python的查找顺序为：局部命名空间->全局命名空间->内置命名空间。
# 如果找不到变量runoob,它将放弃查找并引发一个NameError异常。

# 命名空间的生命周期
# 命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期结束。因此我们无法从外部命名空间访问内部命名空间对象。

# var1是全局名称
# var1 = 5
# def some_func():
#     # var2是局部名称
#     var2 = 6
#     def some_inner_func():
#         # var3是内嵌的局部名称
#         var3 = 7

# 作用域：作用域就是一个python程序可以直接访问命名空间的正文区域
# 在一个python程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。
# python中，程序的变量不是在哪个位置都可以访问的，访问权限取决于这个变量是在哪里赋值的。
# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。python的作用域一共有四种。
# L（Local）:最内层，包含局部变量，比如一个函数/方法内部。
# E（Enclosing）:包含了非局部（non-local）也非全局（non-global）的变量。比如两个嵌套函数，一个函数（或类）A里面又包含了一个函数B，
# 那么对于B中的名称来说A中的作用域就为nonlocal。
# G（Global）:当前脚本的最外层，比如当前模块的全局变量。
# B（Built-in）:包含了内建的变量/关键字等，最后被搜索。
# 规则顺序：L-> E -> G -> B。在局部找不到，便会去局部外的局部找（例如闭包），再找不到就回去全局找，再者去内置中找。

# g_count = 0   #全局作用域
# def outer():
#     o_count = 1   #闭包函数外的函数中
#     def inner():
#         i_count = 2   #局部作用域
# 内置作用域是通过一个名为builtin的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能使用它。
print(dir(builtins))
# python中只有模块（module）,类（class）以及函数（def,lambda）才会引入新的作用域，其它代码块（如if/elif/else,try/except,for/while等）是不会引入新的作用域的，
# 也就是说这些语句内定义的变量，外部也可以访问，如下代码：
if True:
    msg = "I'm from runoob."

print(msg)
# 实例msg变量定义在if语句块中，但外部还是可以访问的。
# 如果将msg定义在函数中，则它就是局部变量，外部不能访问。
# def test():
#     msg_inner = "I'm from runoob."
# print(msg_inner)
# 从报错的信息上看，说明了msg_inner未定义，无法使用。因为它是局部变量，只有在函数内可以使用。

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

total = 0   #这是一个全局变量
# 可写函数说明
def sum(arg1,arg2):
    # 返回两个参数的和
    total = arg1 + arg2    # total在这里是局部变量
    print("函数内是局部变量：",total)
    return total
# 调用sum函数
sum(10,20)
print("函数外是全局变量：",total)

# global和nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字。
# 以下实例修改全局变量num：
num = 1
def fun1():
    global num   #需要使用global关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)

# 如果要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量则需要nonlocal关键字。
def outer():
    num = 10
    def inner():
        nonlocal num     #nonlocal关键字声明
        print(num)
        num = 100
        print(num)
    inner()
    print(num)
outer()

# 另外有一种特殊情况，加入下面这段代码被运行。
# a = 10
# def test():
#     a += 1
#     print(a)
# test()
# 错误信息为局部作用域引用错误，因为test函数中的a使用的是局部，未定义，无法修改。
# 修改a为全局变量
a = 10
def test():
    global a
    a += 1
    print(a)
test()
# 也可以通过函数参数传递
a = 10
def test(a):
    a += 1
    print(a)
test(a)