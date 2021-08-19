# -*- coding：utf-8 -*-
__author__ = "xiaozhu"

import random

# 随机生成1-10之间无序序列整数数据
def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))
    return random_data

# 选择排序
def select_sort(data_list):
    length = len(data_list)

    for i in range(0, length):
        min = i
        # 查找最小的元素
        for j in range(i+1, length):
            if data_list[j] < data_list[min]:
                # 找到最小的元素
                min = j
                # 交换位置
        data_list[min], data_list[i] = data_list[i], data_list[min]

    return data_list

if __name__ == "__main__":

    print("选择排序")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 插入排序
    length = len(random_data)
    sorted_data = select_sort(random_data)

    # 打印排序结果
    print(sorted_data)