# -*-coding:utf-8-*-
#方法是与对象（列表，数，字符串等）联系紧密的函数。
# 通常这样调用方法：object.method(arguments)
#方法调用和函数调用很像，只是在方法名前加上了对象和句点
if __name__ == "__main__":
    # 1.append:方法append用于讲一个对象附加到列表末尾。append就地修改旧列表，不会返回新列表
    a = [1,2,3]
    a.append(4)
    print(a)
    # 2.clear:方法clear就地清空列表内容，类似于切片赋值语句lst[:] = []
    a.clear()
    print(a)
    # 3.copy:方法copy复制列表，常规复制只是将另一个名称关联到列表
    a = [1,2,3]
    b = a
    b[1] = 4
    print(a)
    # 要让a和b指向不同的列表，就必须将b关联到a的副本,这类似于使用a[:]或list(a),它们也都复制a
    a = [1,2,3]
    b = a.copy()
    b[1] = 4
    print(a)
    # 4.count:方法count计算指定的元素在列表中出现了多少次
    x = [[1,2],1,1,[2,1,[1,2]]]
    print(x.count(1))
    print(x.count([1,2]))
    # 5.extend:方法extend让你能够同时将多个值附加到列表末尾，为此可将这些值组成的序列作为参数提供给方法extend.换而言之，你可以用一个列表来扩展另一个列表。
    a = [1, 2, 3]
    b = [4, 5, 6]
    a.extend(b)
    print(a)
    #这可能看起来类似于拼接，但存在一个重要区别，修改了被扩展的序列，在常规的拼接中返回的是一个全新的序列。
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a + b)
    print(a)
    #拼接出来的列表与前一个示例扩展得到的列表完全相同，但这里a并没被修改。鉴于常规拼接必须使用a和b的副本创建一个新的列表，因此要获得类似的效果，拼接的效率将比extend低
    #另外拼接操作并非就地执行的，即它不会修改原来的列表，要获得与extend相同的效果，可将列表赋给切片。
    a = [1, 2, 3]
    b = [4, 5, 6]
    a[len(a):] = b
    print(a)
    # 6.index:方法index在列表中查找指定值第一次出现的索引
    knights = ['are', 'you', 'Who', 'the', 'say', 'Hello']
    print(knights.index('Who'))
    # print(knights.index('World'))
    # 7.insert:方法insert用于将一个对象插入列表
    numbers = [1, 2, 3, 4, 5, 6]
    numbers.insert(3, 'four')
    print(numbers)
    # 与extend一样也可以使用切片赋值来获得与insert一样的效果
    numbers = [1, 2, 3, 4, 5, 6]
    numbers[3:3] = ['four']
    print(numbers)
    # 8.pop:方法pop从列表中删除一个元素（末尾为最后一个元素），并返回这一元素
    x = [1, 2, 3]
    print(x.pop())
    print(x)
    print(x.pop(0))
    print(x)
    # pop是唯一既修改列表又返回一个非None值的列表方法，使用pop可实现一种常见的数据结构--栈（stack）--后进先出
    # push和pop是大家普遍接受的两种栈操作（加入和取走）的名称。python没有提供push，但可以使用append来代替。方法pop和append的效果相反，因此将刚弹出的值压入（或附加）后，得到的栈将与原来相同。
    x  = [1, 2, 3]
    x.append(x.pop())
    print(x)
    # 9.remove:方法remove用于删除第一个为指定值的元素。remove是就地修改且不返回值的方法之一。
    x = ['to', 'be', 'not', 'to', 'be']
    x.remove('be')
    print(x)
    # 10.reverse: 方法reverse按相反的顺序排列列表中的元素。
    x = [1, 2, 3]
    x.reverse()
    print(x)
    # 如果要按相反的顺序迭代序列，可使用函数reversed.这个函数不返回列表，而是返回一个迭代器，可以使用list将返回的对象转换为列表。
    x = [1, 2, 3]
    print(list(reversed(x)))
    # 11.sort:方法sort用于列表就地排序。就地排序意味着对原来的列表进行修改，使其元素按顺序排列，而不是返回排序后列表的副本。
    x = [4, 6, 2, 1, 7, 9]
    x.sort()
    print(x)
    #前面介绍了多个修改列表但不返回任何值的方法，为获取排序后列表的副本，另一种方式是使用函数sorted,这个函数可用于任何序列，但总是返回一个列表。
    x = [4, 6, 2, 1, 7, 9]
    y = sorted(x)
    print(x)
    print(y)
    print(sorted('python'))
    # 12.高级排序  方法sort接受两个可选参数key和reverse,参数key类似于参数cmp:你将其设置为一个用于排序的函数。
    # 然而不会直接使用这个元素是否比另一个元素小，而是使用它来为每个元素创建一个键，再根据这个键对元素排序。
    # 对于另一个关键字参数reverse，只需要将其指定为一个布尔值（True和False）
    # 函数sorted也接受参数key和reverse.在多数情况下，将参数key设置为一个自定义函数很有用。
    x = ['abc', 'chgbju', 'dhskaj', 'asudu', 'dsgta', 'dashdf']
    x.sort(key = len)
    print(x)

    x = [6, 4, 8, 2, 1]
    x.sort(reverse = True)
    print(x)