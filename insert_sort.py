# -*- coding：utf-8 -*-
__author__ = "xiaozhu"

import random

# 随机生成1-1000之间无序序列整数数据
def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))
    return random_data

# 插入排序
def insert_sort(data_list):
    # 序列长度
    lenght = len(data_list)

    for i in range(1, lenght):
        key = data_list[i]
        j = i - 1
        while j>=0:
            # 比较，进行插入排序
            if data_list[j] > key:
                data_list[j+1] = data_list[j]
                data_list[j] = key
            j = j - 1

    return data_list

if __name__ == "__main__":

    print("插入排序")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 插入排序
    sorted_data = insert_sort(random_data)

    # 打印排序结果
    print(sorted_data)