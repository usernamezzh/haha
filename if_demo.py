# _*_ coding:utf-8_*_
if __name__ == "__main__":
    x = int(input("please enter an integer:"))
    if x < 0:
        x = 0
        print(x, "negative charged to zero")
    elif x == 0:
        print("Zero")
    elif x  == 1:
        print("single")
    else:
        print("more")

