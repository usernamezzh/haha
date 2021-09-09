# -*-coding:utf-8-*-

import sys

# 迭代器（迭代是python最强大功能之一，是访问集合元素的一种方式）
# 迭代器是可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完结束。迭代器只能往前，不能后退。
# 迭代器有两个基本的方法iter()和next()

# 字符串、列表、元组对象都可以用于创建迭代器。
def Iter(list):
    it = iter(list)
    print(next(it))
    print(next(it))
    return

# 迭代器对象可以使用常规for语句进行遍历
def Iterfor(list):
    it = iter(list)
    for x in it:
        print(x, end = " ")
    return

# 也可使用next()函数
def Iternext(list):
    it = iter(list)
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()
    return

# 创建一个迭代器（把一个类作为一个迭代器使用需要在类中实现两个方法__iter__()与__next__()）
class myNumberes:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


if __name__ == "__main__":
    # list = [1,2,3,4]
    # Iter(list)
    #
    # Iterfor(list)
    # print()
    #
    # Iternext(list)

    myclass = myNumberes()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))

    Myclass = MyNumbers()
    Myiter = iter(Myclass)

    for x in Myiter:
        print(x)