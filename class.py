# -*-coding:utf-8-*-

# 面向对象技术简介
# 类（class）:用来描述具有相同属性和方法的对象的集合，它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 方法：类中定义的函数。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override）,也称为方法的重写。
# 局部变量：定义在方法中的变量，只作用于当前实例的类。
# 实例变量：在类的声明中，属性是用变量来表示的，这种变量称为实例变量，实例变量就是一个用self修饰的变量。
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如：有这样一个设计，
# 一个Dog类型的对象派生自Animal类，这是模拟“是一个（is-a）”关系（例图，Dog是一个Animal）。
# 实例化：创建一个类的实例，类的具体对象。
# 对象：通过类定义的数据结构实例，对象包括两个数据成员（类变量和实例变量）和方法。
# python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。

# 类定义：
# class ClassName：
#     <statement -1>
#     .
#     .
#     .
#     <statement -n>
# 类实例化后可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性。

# 类对象 类对象支持两种操作：属性引用和实例化。
# 属性引用使用和python中所有的属性引用一样的标准语法：obj.name。
# 类对象创建后，类命名空间中所有的命名都是有效属性名。

class MyClass:
    i = '123456'
    def f(self):
        return 'Hello World!'

x = MyClass()

print("MyClass类的属性i为：",x.i)
print("MyClass类的方法f输出为：",x.f())

# 类有一个名为__init__()的特殊方法（构造方法），该方法在类实例化时会自动调用，像下面这样：
def __init__(self):
    self.data = []
# 类定义了__init__()方法，类的实例化操作会自动调用__init__()方法。
# 当然，__init__()方法可以有参数，参数通过__init__()传递到类的实例化操作上。

class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0,-4.5)

print(x.r, x.i)

# self代表类的实例，而非类
# 类的方法与普通的函数只有一个普通的区别--它们必须有一个额外的第一个参数名称，按照惯例它的名称是self.
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

# 从执行结果可以很明显的看出，self代表的是类的实例，代表当前对象的地址，而self.class则指向类。
# self不是python关键字，我们把他换成runoob也是可以正常执行的。

class Test1:
    def prt(Runoob):
        print(Runoob)
        print(Runoob.__class__)
t1 = Test1()
t1.prt()

# 类的方法
# 在类的内部，使用def关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数，self代表的是类的实例。
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，私有属性在类外部无法直接访问
    __weight = 0
    #定义构造函数
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说：我%d岁,%dKG。"%(self.name,self.age,self.__weight))

# 实例化类
p = people("Runoob",10,30)
p.speak()

# 继承
# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     .
#     .
#     <statement-n>
# 子类（派生类DerivedClassName）会继承父类（基类BaseClassName）的属性和方法
# BaseClassName(实例中的基类名)必须与派生类定义在一个作用域内。除了类还可以用表达式，基类定义在另一个模块中时这一点非常有用。
# class DerivedClassName(modname.BaseClassName):
class people1:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接访问
    __weight = 0
    # 定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说：我%d岁。"%(self.name,self.age))

# 单继承示例
class student(people1):
    grade = 0
    def __init__(self,n,a,w,g):
        # 调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade = g
    # 覆写父类的方法
    def speak(self):
        print("%s说：我%d岁，我读%d年级。"%(self.name,self.age,self.grade))

s = student("Tom", 10, 30, 3)
s.speak()

# 多继承
# class DerivedClassName(Base1,Base2,Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-n>
# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索即方法在子类中未找到时，从左到右查找父类中是否包含方法。
class people2:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接访问
    __weight = 0
    # 定义构造函数
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说：我%d岁，体重%dkg。"%(self.name,self.age,self.__weight))

# p1 = people2("Tom",10,30)
# p1.speak()
# 单继承示例
class student(people2):
    grade = 0
    def __init__(self,n,a,w,g):
        # 调用父类函数
        people2.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print("%s说：我%d岁，我今年%d年级"%(self.name,self.age,self.grade))
# s1 = student("Tony", 15, 50, 8)
# s1.speak()
# 另一个类，多重继承前的准备
class speaker:
    # 定义基本属性
    name = ''
    topical = ''
    # 定义构造函数
    def __init__(self,n,t):
        self.name = n
        self.topical = t
    def speak(self):
        print("我的名字叫%s，是一名演说家，今天演说的主题是%s"%(self.name,self.topical))
s2 = speaker('Tim','python')
s2.speak()

# 多重继承
class sample(speaker,student):
    def __init__(self,n,a,w,g,t):
        # 调用父类函数
        speaker.__init__(self,n,t)
        student.__init__(self,n,a,w,g)
s3 = sample('Nancy',15,30,7,'python')
s3.speak()  #方法名相同，默认调用的是在括号排前的父类的方法

# 方法重写
# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法。
class Parent: #定义父类
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):  #定义子类
    def myMethod(self):
        print('调用子类方法')

C = Child()    #子类实例
C.myMethod()   #子类调用重写方法
super(Child,C).myMethod() #用子类对象调用父类已被覆盖的方法
# super() 函数是用于调用父类（超类）的一个方法


# 类属性与方法
# 类的私有属性：_private_attrs:两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问，在类内部的方法中使用时self._private_attrs。
# 类的方法：在类的内部使用关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数，self代表的是类的实例。
# self的名字并不是规定死的，也可以使用this，但是最好按照约定使用self。
# 类的私有方法：_private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用，不能在类的外部调用。self._private_methods。

class JustCounter:
    __secretCount = 0   # 私有变量
    publicCount = 0     # 公有变量
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__sercret)  # 报错，实例不能访问私有对象

class site:
    name = ''
    url = ''
    def __init__(self,name,url):
        self.name = name
        self.url = url

    def who(self):
        print("name:",self.name)
        print("url:",self.url)

    def __foo(self):
        print("这是私有方法")

    def foo(self):
        print("这是公有方法")
        self.__foo()

x = site("菜鸟教程", "www.runoob.com")
x.who()
x.foo()
# x.__foo()   #报错，外部不能调用私有方法

# 类的专有方法：
# __init__: 构造函数，在生成对象时调用
# __del__: 析构函数，释放对象时调用
# __repr__: 打印，转换
# __setitem__: 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获取长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__:  加运算
# __sub__:  减运算
# __mul__:  乘运算
# __truediv__:  除运算
# __mod__:  求余运算
# __pow__:  乘方

# 运算符重载
# python同样支持运算符重载，我们可以对类的专有方法进行重载

class vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'vector (%d,%d)' %(self.a, self.b)

    def __add__(self,other):
        return vector(self.a + other.a, self.b + other.b)

v1 = vector(5,10)
v2 = vector(5,-2)
print(v1 + v2)



