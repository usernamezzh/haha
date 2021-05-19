# -*-coding:utf-8-*-
if __name__ == "__main__":
    database = [
        ['test', 'a123456'],
        ['Tom', '123456'],
        ['Haha', 'b123456'],
        ['Hehe', 'c123456']
    ]
    UserName = input('user name:')
    Pin = input('Pin Code:')
    if [UserName, Pin] in database:
        print('Access granted')
    else:
        print('UserName inexistence')
