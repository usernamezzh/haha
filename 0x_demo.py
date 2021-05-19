# -*-coding:utf-8-*-
author = "xiaohong"

# python 2进制、8进制、10进制、16进制表示方法与转化
if __name__ == "__main__":
    # 2进制 满2进1 0b1
    # 8进制 满8进1 0o1
    # 10进制 满10进1 10
    # 16进制 满16进1 0x1
    # bin() 转2进制方法     int()转10进制方法     oct()转8进制方法     hex()转16进制方法
    print(0b11)
    print(0o11)
    print(10)
    print(0xAF)
    print(bin(10))
    print(bin(0o11))
    print(bin(0xAF))
    print(int(0b11))
    print(int(0o11))
    print(int(0xAF))
    print(oct(0b11))
    print(oct(10))
    print(oct(0xAF))
    print(hex(0b11))
    print(hex(0o11))
    print(hex(20))