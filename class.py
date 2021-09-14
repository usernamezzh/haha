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
