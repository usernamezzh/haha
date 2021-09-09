# -*-coding:utf-8-*-
'''
函数是组织好的，可重复使用的，用来实现单一或相关联功能的代码段
函数能提高应用的模块性，和代码的重复利用率。

定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则
1.函数代码块以def关键字开头，后接函数标志符名称和圆括号（）
2.任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
3.函数第一行语句可以选择性的使用文档字符串-用于存放函数说明。
4.函数内容以冒号:起始，并且缩进。
5.return[表达式]结束函数，选择性的返回一个值给调用方，不带表达式的return相当于返回None
'''
def hello():
    print("hello World!")

def max(a,b):
    if a > b:
        return a
    else:
        return b

def area(width, height):
    return width * height

# 函数调用：定义了一个函数（给了函数一个名称，指定了函数里包含的参数和代码块结构），这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从python命令提示符执行。
def printme(str):
    print(str)
    return

# 参数传递：在python中，类型属于对象，变量是没有类型的。
# a = [1,2,3]     a = 'string'   [1,2,3]是list类型，'string'是String类型，而变量a是没有类型，它仅仅是一个对象的引用（一个指针），是一个可以指向list类型对象，也可以是一个指向String类型对象
# 可更改和不可更改对象：在python中，String、tuple和number是不可更改的对象，list和dict是可更改的对象
# 不可变对象：变量a = 5后再赋值a = 10,这里实际是新生成一个int值对象10，再让a指向它，而5被丢弃，不是改变a的值，相当于新生成了a.
# 可变类型：变量赋值la=[1,2,3,4]后再赋值la[2]=5,则是将list la的第三个元素值更改，本身la没动，只是其内部一部分值被修改了。
# 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
# 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响。
# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

# python传不可变对象实例
def change(a):
    print(id(a)) #通过id()函数查看内存地址变化
    print(a)
    a = 10
    print(id(a))
    print(a)

# python传可变对象实例
def changeme(mylist):
    print(id(mylist))
    mylist.append([1,2,3,4,5])
    print("函数内取值：",mylist)
    print(id(mylist))
    return mylist

# 参数（必须参数、关键字参数、默认参数、不定长参数）
# 必须参数（必须参数需以正确的顺序传入函数，调用时的数量必须和声明时的一样）

# 关键字参数（关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为python解释器能够用参数名匹配参数值）

# 默认参数（调用函数时，如果没有传递参数，则会使用默认参数。）
def printinfo(name, age = 30):
    print("名字", name)
    print("年龄", age)
    return

# 不定长参数（一个函数处理比当初声明时更多的参数，这些参数叫不定长参数）
# def functionname([formal_args,] *var_args_tuple ):
#     "函数_文档字符串"
#     function_suite
#     return [expression]
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printInfo(arg1, *vartuple):
    print(arg1)
    print(vartuple)
# 声明函数时，参数中星号 * 可以单独出现，例如:
# 如果单独出现星号 * 后的参数必须用关键字传入。
def F(a, b, *, c):
    print(a + b + c)

# 还有一种就是参数带两个星号 **基本语法如下：
# def functionname([formal_args,] **var_args_dict ):
#     "函数_文档字符串"
#     function_suite
#     return [expression]
# 加了两个星号 ** 的参数会以字典的形式导入。
def f(arg1, **vardict):
    print(arg1)
    print(vardict)

if __name__ == "__main__":
    hello()
    print(max(5,4))
    print(area(5,4))
    printme("我调用了一次函数")
    printme(str = "我再次调用了函数")

    a = 1
    change(a)
    print(id(a))     #可以看见在调用函数前后，形参和实参指向的是同一个对象（对象id相同），在函数内部修改形参后，形参指向的是不同的id

    mylist = [10, 20, 30]
    changeme(mylist)
    print("函数外取值：", mylist)     #可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。
    print(id(mylist))
    print(mylist[3][3])

    printinfo(age = 50,  name = "小红")
    printinfo("小华")

    printInfo(10,20,30)

    f(1,a = 2, b = 3)

    F(1,2,c=3)