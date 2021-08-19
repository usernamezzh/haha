# -*- coding：utf-8 -*-
__author__ = "xiaozhu"

import random

# 随机生成1-1000之间无序序列整数数据
def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data

# 快速排序
def quick_sort(lists, left, right):
    '''快速排序'''
    # 跳出递归判断
    if left >= right:
        return lists

    # 选择参考点，该调整范围的第1个值
    key = lists[left]
    low = left
    high = right

    # 循环判断直到遍历全部
    while left < right:
        # 从右边开始查找大于参考点的值
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]  # 这个位置的值先挪到左边

        # 从左边开始查找小于参考点的值
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]  # 这个位置的值挪到右边

    # 写回改成的值
    lists[left] = key

    # 递归，并返回结果
    quick_sort(lists, low, left - 1)    # 递归左边部分
    quick_sort(lists, left + 1, high)   # 递归右边部分
    return lists

if __name__ == "__main__":

    print("快速排序")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 插入排序
    length = len(random_data)
    sorted_data = quick_sort(random_data, 0, length-1)

    # 打印排序结果
    print(sorted_data)
