# -*-coding:utf-8-*-
# 变量可变类型和不可变类型
# 不可变类型：数字类型（int，float,bool, complex,long）   字符串类型（str）    元组（tuple）
# 可变类型：列表（list）   字典（dict）
if __name__ == "__main__":
    list = [1, 2, 3]
    print("定义列表前列表地址为%d"%id(list))
    list.append(999)
    list.pop(0)
    list.remove(2)
    list[0] = 10
    print(list)
    print("修改数据后的内存地址为%d"%id(list))

    dict = {"name":"小明"}
    print("定义字典后的内存地址为%d"%id(dict))
    dict["age"] = 18
    dict.pop("name")
    dict["name"] = "老王"
    print(dict)
    print("修改数据后的内存地址为%d"%id(dict))