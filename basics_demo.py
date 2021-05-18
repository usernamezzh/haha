# -*-coding:utf-8-*-
#1.关键字
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import
# ', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#2.注释

#3.获取键盘输入
# if __name__ == "__main__":
#     #获取键盘输入
#     date = input("请输入:")
#     #通过空格切割输入数据
#     list_date = date.split(" ")
#     #打印键盘的输入
#     print("您输入的是:%s"%list_date)

#4.命令行参数
import sys
if __name__ == "__main__":
    print("命令行参数个数:%d"%len(sys.argv))
    print("命令行参数列表:%s"%str(sys.argv))
    input('press<Enter>')