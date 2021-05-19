# -*-coding:utf-8-*-
# 字典：通过名称来访问各个值的数据结构，这种数据结构称为映射。字典是python中唯一的内置映射类型。其中的值不按顺序排列，而是存储在键下。键可能是数、字符串和元组。

if __name__ == "__main__":
    # 1.字典的创建和用途
    phonebook = {"Alice":"2351", "Beth":"5286", "Alean":"8126"}
    # 字典是由键和相应的值组成，这种键-值对称为项，每个键与其值用：分隔，项之间用，分隔，整个字典放在{}内。空字典：{}
    # 在字典以及其它映射类型中，键必须是独一无二的，而字典中的值无需如此。
    print(phonebook["Alice"])

    # 2.dict的使用：可使用函数dict从其它映射（如其它字典）或键值对序列创建字典。
    items = [("name", "Tom"),("age", 41)]
    print(dict(items))
    # 还可使用关键字实参来调用这个函数
    print(dict(name = "Tom", age = 41))

    # 3.基本的字典操作
    # len(d)返回字典d包含的项（键-值对）数
    # d[k]返回与键k相关联的值
    # d[k] = v将值v关联到键k
    # del d[k]删除键为k的项
    # k in d检查字典d是否包含键为k的项
    # 虽然字典与列表有多个相同之处，但也有一些重要的不同之处。与list,tuple和str一样，dict不是函数，而是一个类。
    # 键的类型：字典键的类型可以是整数，但并非必须是整数。字典中的键可以是任何不可变的类型，如浮点数（实数），字符串或元组。
    # 自动添加：即便是字典中原本没有的键，也可以给它赋值，这将在字典中创建一个新项。然而，如果不使用append或其它类似方法，就不能给列表中没有的元素赋值。
    # 成员资格：表达式k in d(其中d是一个字典)查找的是键而不是值，而表达式v in l（其中l是一个列表）查找的是值而不是索引。这看似不太一致，但你习惯后就会觉得相当自然。毕竟如果字典包含指定的键，检查相应的值就很容易。
    # 相比于检查列表是否包含指定的值，检查字典是否包含指定的键的效率更高。数据结构越大，效率差距就越大。
    # x = []
    # x[42] = "Foobar"
    # print(x[42])

    x = [None] * 43
    x[42] = "Foobar"
    print(x[42])

    # 一个将人名用作键的字典，每个人都用一个字典表示。
    # 字典包含键“phone”和“addr”,它们分别与电话号码和地址相关联
    people = {
        "Alice":{
            "phone":"2563",
            "addr":"Foo drive 23"
        },
        "Beth":{
            "phone":"5241",
            "addr":"Bar street 42"
        },
        "Cecil":{
            "phone":"1253",
            "addr":"Baz avenue 51"
        }
    }
    # 电话号码和地址的描述性标签，供打印输出时使用。
    labels = {
        "phone":"phone number",
        "addr":"address"
    }
    name = input("Name: ")

    #要查找电话号码还是地址
    request = input("phone number (p) or address (a)?")

    #使用正确的键：
    if request == "p":
        key = "phone"
    if request == "a":
        key = "addr"

    #仅当名字是字典包含的键时才打印信息
    if name in people:
        print("{}'s {} is {}.".format(name,labels[key],people[name][key]))

    #将字符串格式设置功能用于字典
    phonebook = {"Alice":"3251", "Beth":"5286", "Cecil":"8563"}
    print("Cecil's phone number is {Cecil}.".format_map(phonebook))

    template = """<html>
    <head><title>{title}</title></head>
    <body>
    <h1>{title}</h1>
    <p>{text}</p>
    </body>
    """
    data = {"title":"My home page", "text":"Welcome to my home page!"}
    print(template.format_map(data))

    #字典方法