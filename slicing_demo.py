# -*-coding:utf-8-*-
if __name__ == '__main__':
    tag = '<a href="http://www.python.org">python web site</a>'
    print(tag[9:30])
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(numbers[3:6])
    print(numbers[0:1])
    print(numbers[7:10])
    print(numbers[-3:-1])
    print(numbers[-3:0])
    print(numbers[-3:])
    print(numbers[:3])
    print(numbers[:])
    print(numbers[8:3:-1])
    print(numbers[0:100])
    print(numbers[0:10:1])
    print(numbers[0:10:2])
    print(numbers[::4])
    print(numbers[8:3:-1])
    print(numbers[::-2])
    print(numbers[10:0:-2])
    print(numbers[0:10:-2])
    print(numbers[5::-2])
    print(numbers[:5:-2])

    url = input('please input url:')
    domain = url[11:-4]
    print(domain)