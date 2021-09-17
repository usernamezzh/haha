# -*-coding:utf-8-*-

import os
import shutil
import glob
import sys
import re
import math
import random
from urllib.request import urlopen
import datetime
from datetime import date
import time
import zlib
from timeit import Timer
import doctest
import unittest

# 操作系统接口
# os模块提供了不少与操作系统相关联的函数
print(os.getcwd())   #返回当前的工作目录
# os.chdir('D:\program Files')  #修改当前的工作目录
# os.system('mkdir today')   #执行系统命名mkdir
# 建议使用import os,而非from os import *。这样可以保证随操作系统不同而有所变化的os.open()不会覆盖内置函数open()。
# 在使用os这样的大型模块时内置的help()和dir()函数非常有用。
print(dir(os))
# print(help(os))

# 针对日常的文件和目录管理任务，shutil模块提供了一个易于使用的高级接口
# shutil.copyfile(r"C:\Users\Administrator\Desktop\test.txt",r"C:\Users\Administrator\Desktop\test2.txt")
# shutil.move(r"C:\Users\Administrator\Desktop\test.txt",r'C:\Users\Administrator\Desktop\U盘')

# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
print(glob.glob('*.py'))

# 命令行参数
# 通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于sys模块的argv变量。
print(sys.argv)

# 错误输出重定向和程序终止
# sys还有stdin,stdout和strerr属性，即使在stdout被重定向时，或者也可以用于显示警告和错误信息。
sys.stderr.write("warning,log file not found starting a new one\n")
# 大多数脚本定向终止都使用“sys.exit()”。

# 字符串正则匹配
# re模块为高级字符串提供了正则表达式工具。对于复杂的匹配和处理,正则表达式提供了简洁，优化的解决方案。
print(re.findall(r"\bf[a-z]*",'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# 如果只需要简单的功能，应该首先考虑字符串方法，因为非常检单，易于调试和阅读。
print('tea for too'.replace('too','two'))

# 数学 math模块为浮点运算提供了对底层C函数库的访问
print(math.cos(math.pi/4))
print(math.log(1024,2))

# random提供了生成随机数的工具
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100),10))
print(random.random())  # random float
print(random.randrange(100))

# 访问互联网
# 有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)

# 日期和时间
# datetime模块为日期和时间处理同时提供了简单和复杂的方法。
# 支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
# 该模块还支持时区处理
# 今天 today = datetime.date.today()
print(datetime.date.today())
# 昨天 yesterday = today - datetime.timedelta(days = 1)
print(datetime.date.today() - datetime.timedelta(days = 1))
# 当前时间戳 time_stamp = time.time()
time_stamp = time.time()
print(time_stamp)

# 数据压缩 zlib,gzip,bz2,zipfile以及tarfile模块直接支持通用的数据打包和压缩格式
s  = b'witch which has which witchs wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))

# 性能度量
# 有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
# 例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,timeit 证明了现代的方法更快一些。
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a, b = b, a','a = 1; b = 2').timeit())

# 测试模块
# 开发高质量软件的方法之一是为每个函数开发测试代码，并且在开发过程中经常进行测试。
# doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
# 测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。
# 通过用户提供的例子，它强化了文档。允许doctest模块确认代码的结果是否与文档一致。
def average(values):
    """
    computes the arithmetic mean of a list of numbers.
    print(average[20,30,50])
    40
    """
    return sum(values)/len(values)

doctest.testmod() # 自动验证嵌入测试

# unittest模块不像doctest模块那么容易使用，不过它可以在一个独立的文件夹里提供一个更全面的测试集
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20,30,70]),40)
        self.assertEqual(round(average([1,5,7]),1),4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests
