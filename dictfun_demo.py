# -*-coding:utf-8-*-
from copy import deepcopy

if __name__ == "__main__":
    # 1.clear方法：方法clear删除所有的字典项，这种操作是就地执行的（就像list.sort一样），因此什么都不返回（或者说返回None）。
    d = {}
    d["name"] = "Gumby"
    d["age"] = 41
    print(d)
    returned_value = d.clear()
    print(d)
    print(returned_value)

    # 在这两个场景中，x和y最初都指向同一个字典。在第一个场景中，我通过将一个空字典赋
    # 给x来“清空”它。这对y没有任何影响，它依然指向原来的字典。这种行为可能正是你想要的，
    # 但要删除原来字典的所有元素，必须使用clear。如果这样做，y也将是空的，如第二个场景所示。
    # 场景1
    x = {}
    y = x
    x["key"] = "value"
    print(y)
    x = {}
    print(x)
    print(y)

    # 场景2
    x = {}
    y = x
    x["key"] = "value"
    print(y)
    x.clear()
    print(x)
    print(y)

    # 2.copy方法：方法copy返回一个新字典，其中包含的键-值对与原来的字典相同（这个方法执行的是浅复制，因为值本身是原件，而非副本）
    x = {"UserName":"Admin", "machines":['For', 'Bar', 'Baz']}
    y = x.copy()
    y["UserName"] = "haha"
    y["machines"].remove("Baz")
    print(y)
    print(x)
    #如你所见，当替换副本中的值时，原件不受影响。然而如果修改副本中的值（就地修改而不是替换），原件也将发生变化，因为原件指向的也是被修改的值。
    #为避免这种问题，一种方法是执行深复制，即同时复制值及其包含的所有值。deepcopy
    d = {}
    d["name"] = ["Tom", "Nancy", "Mary"]
    c = d.copy()
    dc = deepcopy(d)
    d["name"].append("Tony")
    print(c)
    print(dc)

    # 3.fromkeys方法：方法fromkeys创建一个新字典，其中包含指定的键，且每个键对应的值都是None。
    print({}.fromkeys(["name", "age"]))
    print(dict.fromkeys(["name","age"]))
    print(dict.fromkeys(["name","age"],"unknown"))

    # 4.get方法：试图访问字典中没有的项，将引发错误。使用get来访问不存在的键时，没有引发异常，而是返回None。你可指定默认值，这样将返回你指定的值，而不是None。
    x = {}
    # print(x["name"])
    print(x.get("name"))
    print(x.get("name","N/A"))
    print(x.get("name","Elic"))

    #一个使用get的简单数据库
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
    labels = {
        "phone":"phone number",
        "addr": "address"
    }
    name = input("Name: ")
    request = input("Phone number (p) or address (a)")
    key = request
    if request == "p":
        key = "phone"
    if request == "a":
        key = "addr"
    person = people.get(name,{})
    label = labels.get(key,key)
    result = person.get(key,"not available")
    print("{}'s {} {}.".format(name, label, result))

    # 5.items方法：方法items返回一个包含所有字典项的列表，其中每个元素都为（key,value）的形式，字典项在列表中的排列顺序不确定。
    # 返回值属于一种名为字典视图的特殊类型，字典视图可用于迭代。
    d = {"title":"Python Web Site", "url":"http://www.python.com", "spam":0}
    print(d.items())
    print(len(d.items()))
    print(("spam" , 0) in d.items())
    #字典视图的一个优点是不复制，它们始终是底层字典的反映，即便你修改了底层字典亦如此。
    d["spam"] = 1
    print(("spam, 0") in d.items())
    d["spam"] = 0
    print(("spam, 0") in d.items())

    #6.keys方法:返回一个字典视图，其中包含指定字典中的键。

    #7.pop方法：方法pop可用于获取与指定键相关联的值，并将该键-值对从字典中删除。
    d = {"x" : 1, "y" : 2}
    print(d.pop("x"))
    print(d)

    #8.popitem方法：方法popitem类似于list.pop,但list.pop弹出list的最后一个元素，而popitem随机的弹出一个字典项，因为字典项的顺序是不确定的，没有最后一个元素的概念。
    # 如果你要以高效地方式逐个删除并处理所有字典项，这可能很有用，因为这样无需先获取键列表。
    d = {"url" : "http://www.python.com", "spam" : 0, "title" : "Python Web Site"}
    print(d.popitem())
    print(d)

    #9.setdefault方法：方法setdefault有点像get，因为它也获取与指定键相关联的值，但除此之外，setdefault还在字典不包含指定的键时，在字典中添加指定的键-值对。
    d = {}
    print(d.setdefault('name', 'N/A'))
    print(d)
    d['name'] = 'Gumby'
    print(d.setdefault('name', 'N/A'))
    print(d)
    # 如你所见，指定的键不存在时，setdefault返回指定的值并相应地更新字典。如果指定的键
    # 存在，就返回其值，并保持字典不变。与get一样，值是可选的；如果没有指定，默认为None。
    d = {}
    print(d.setdefault('name'))
    print(d)

    #10.update方法：方法update使用一个字典中的项来更新另一个字典。
    d = {
        'title': 'Python Web Site',
        'url': 'http://www.python.org',
        'changed': 'Mar 14 22:09:15 MET 2016'
    }
    x = {'title': 'Python Language Website'}
    print(d.update(x))
    print(d)
    # 对于通过参数提供的字典，将其项添加到当前字典中。如果当前字典包含键相同的项，就替换它。
    # 可像调用本章前面讨论的函数dict（类型构造函数）那样调用方法update。这意味着调用
    # update时，可向它提供一个映射、一个由键值对组成的序列（或其他可迭代对象）或关键字参数

    #11.values方法：方法values返回一个由字典中的值组成的字典视图。不同于方法keys，方法values返回的视图可能包含重复的值。
    d = {}
    d[1] = 1
    d[2] = 2
    d[3] = 3
    d[4] = 1
    print(d.values())
