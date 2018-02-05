# -*- coding: utf-8 -*-

# 找数组中最小数
# 入：数组
# 出：最小元素下标
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 选择排序 - 一个一个
# 入：数组
# 出：由小到大排序的数组
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# 快速排序 - 找基准值分大小数组
# 入：数组
# 出：由小到大排序的数组
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]   # 由所有小于等于基准值的元素组成的子数组
        greater = [i for i in arr[1:] if i > pivot]   # 由所有大于基准值的元素组成的子数组
        return quickSort(less) + [pivot] + quickSort(greater)

print selectionSort([5, 3, 6, 2, 10])
print quickSort([5, 3, 6, 2, 10])