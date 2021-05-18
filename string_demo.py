# _*_ coding:utf-8 _*_
if __name__ == "__main__":
    # print('spam eggs')
    # print('doesn\'t')   #'\'转义字符
    # print("doesn't")
    # print('"Yes," they said.')
    # print("\"Yes,\" they said.")   #'\'转义字符
    # print('"Isn\'t," they said')
    # print('C:\some\name')   #here \n means newline
    # print(r'C:\same\name')   #note the r before the quote
    # print("""\
    # Usage:things[OPTIONS]
    # -h
    # -H hostname
    # """)
    # print("""
    # Usage:things[OPTIONS]
    # -h
    # -H hostname
    # """)
    print(3 * 'um' + 'ium')
    print('py' 'thon')
    # prefix = 'py'
    # print(prefix 'thon')   # can't concatenate a variable and a string literal
    print('um' *3)
    # print('um' * 3 'ium')
    print('um' * 3 + 'ium')
    prefix = 'py'
    print(prefix + 'thon') #If you want to concatenate variables or a variable and a literal, use +:
    word = 'python'
    print(word[0])
    print(word[-1])
    print(word[0:2])
    print(word[2:5])
    print(word[:2] + word[2:])
    # print(word[35]) #Attempting to use an index that is too large will result in an error
    print(word[2:42])
    print(word[42:])
    # word[0] = 'J' #Python strings cannot be changed — they are immutable.
    print('J' + word[2:])
    print(len('qghuytvbkm'))
