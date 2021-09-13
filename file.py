# -*-coding:utf-8-*-
import pickle

str = input("请输入内容：")
print("输入的内容是：", str)

# 读和写文件
# open()将会返回一个file对象，基本语法open(filename, mode)
# filename:包含了要访问的文件名称的字符串值
# mode:决定了打开文件的模式：只读、写入、追加等。这个参数是非强制的，默认文件访问模式为只读（r）。
# 模式：r      描述：以只读方式打开，文件的指针将会放在开头。这是默认模式。
# 模式：rb     描述: 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
# 模式：r+     描述：打开一个文件用于读写。文件的指针将会放在文件的开头。
# 模式: rb+    描述：以二进制格式打开一个文件用于读写。文件的指针将会放在文件的开头。
# 模式：w      描述：以只写的方式打开，如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# 模式：wb     描述：以二进制格式打开一个文件用于只写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果文件不存在，创建新文件。
# 模式：w+     描述：打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建该文件。
# 模式: wb+    描述：以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果文件不存在，创建新文件。
# 模式：a      描述：以追加方式打开一个文件。如果该文件已存在，文件指针将会放在文件的结尾。也就是说新内容会被写到原有内容后面。如果该文件不存在，创建新文件进行写入。
# 模式：ab     描述：以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说新内容会被写到原有内容后面。如果该文件不存在，创建新文件进行写入。
# 模式：a+     描述：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件进行读写。
# 模式：ab+    描述：以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件进行读写。

f = open(r"C:\Users\Administrator\Desktop\test.txt","w")
f.write("python是一个非常好的语言。\n是的，的确非常好!\n")
f.close()

# 文件对象的方法
# f.read(size)将读取一定数目的数据，然后作为字符串或字节对象返回。size是一个可选的数字类型的参数，当size被忽略了或者为负，那么该文件的所有内容都将被读取并且返回
f = open(r"C:\Users\Administrator\Desktop\test.txt","r")
str = f.read()
print(str)
f.close()

# f.readline()会从文件中读取单独的一行。换行符为'\n'。f.readline()如果返回一个空字符串，说明已经读取到最后一行。
f = open(r"C:\Users\Administrator\Desktop\test.txt","r")
str = f.readline()
print(str)
f.close()

# f.readlines()将返回该文件中包含的所有行.如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
f = open(r"C:\Users\Administrator\Desktop\test.txt","r")
str = f.readlines()
print(str)
f.close()

# f.write() f.write(string)将string写入都文件中，然后返回写入的字符数。
f = open(r"C:\Users\Administrator\Desktop\test.txt","a")
num = f.write("哈哈哈哈哈哈。\n 呵呵呵呵呵呵呵呵\n")
print(num)
f.close()

f = open(r"C:\Users\Administrator\Desktop\test.txt","r")
str = f.read()
print(str)
f.close()

# f.tell() 返回文件对象当前所处的位置，它是从文件开头开始算起的字节数。
f = open(r"C:\Users\Administrator\Desktop\test.txt","a")
nums = f.tell()
print(nums)
f.close()

# f.seek() 如果要改变文件当前的位置，可以使用f.seek(offset,from_what)函数。
# from_what的值，如果是零表示开头，如果是1表示当前位置，如果是2表示文件的结尾，例如：
# f.seek(x,0):从起始位置即文件首行首字符开始移动x个字符。
# f.seek(x,1):表示从当前位置移动x个字符。
# f.seek(-x,2):表示从文件结尾向前移动x个字符。
f = open(r"C:\Users\Administrator\Desktop\test.txt",'rb+')
print(f.seek(0,0))
print(f.read(1))
print(f.seek(6,1))
print(f.read(1))
print(f.seek(-5,2))
print(f.read(1))
f.close()

# f.close()在文本文件中(那些打开文件模式下没有b的),只会相对于文件起始位置进行定位。当你处理完一个文件后，调用f.close()来关闭文件并释放系统的资源，如果再次尝试调用该文件，则会抛出异常。
# 当处理一个文件对象时，使用with关键字是非常好的方式。在结束后它会帮你正确的关闭文件。而且写起也比try-finally语句块要简短。
with open(r"C:\Users\Administrator\Desktop\test.txt","r") as f:
    read_data = f.read()
    print(read_data)
print(f.closed)

# pickle模块  python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块反序列化操作，我们能够从文件中创建上一次程序保存的对象。
# 基本接口：pickle.dump(obj,file,[,protocol])  有了pickle这个对象，就能对file以读取的形式打开
# x = pickle.load(file)   注解：从file中读取一个字符串，并将它重构为原来的python对象。file有read()和readline()接口。

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open(r'C:\Users\Administrator\Desktop\pickle.txt', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()