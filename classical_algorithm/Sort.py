import random

def insert_sort(lists):
    for i in range(1,len(lists)):
        tmp = lists[i]
        for j in range(i-1,-1,-1):
            if lists[j] > tmp:
                lists[j+1] = lists[j] #数据移动
            else:
                break
        lists[j] = tmp        


def select_sort(lists):
    for i in range(0,len(lists)):
        cur_min = i
        for j in range(i, len(lists)):
            if lists[j] < lists[cur_min]:
                cur_min = j
        lists[i],lists[cur_min] = lists[cur_min],lists[i]


def bubble_sort(lists):
    for i in range(len(lists)):
        flag = True
        for j in range(len(lists)-i-1):
            if lists[j] > lists[j+1]:
                lists[j],lists[j+1] = lists[j+1], lists[j]
                flag = False
        if flag:
            break


def merge(left,right):
    i,j = 0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    
    return result



def merge_sort(lists):
    # 递归终止条件 -> 不可再分
    if len(lists) <= 1:
        return lists

    num = len(lists)//2

    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    
    return merge(left,right)    

"""
##  快速实现
from random import choice
   
def quick_sort(lists):
    if len(lists) <= 1:
        return lists
    else:
        pivot = choice(lists)
        return quick_sort([item for item in lists if item < pivot]) + [pivot] + quick_sort([item for item in lists if item > pivot])    
"""



from random import randint
## 就地排序实现
def randomized_partition(lists,left,right):
    
    # 生成随机元素并与 lists 最右边元素进行交换
    pivot = randint(left,right)
    lists[pivot],lists[right] = lists[right],lists[pivot]
    
    i = left
    # 0..i保存着比 pivot 小的所有元素
    for j in range(left,right):
        if lists[j] < lists[right]:
            lists[i],lists[j] = lists[j],lists[i]
            i += 1
    lists[right],lists[i] = lists[i],lists[right]

    return i 

def quick_sort_c(lists, left, right):
    if left >= right:
        return 
    pivot = randomized_partition(lists,left, right)
    quick_sort_c(lists,left,pivot)
    quick_sort_c(lists,pivot+1,right)
        


def quick_sort(lists):
    if len(lists) <= 1:
        return 
    quick_sort_c(lists,0,len(lists)-1)

    


## 基数排序
import math
from functools import reduce
from operator import add
def radix_sort(lists, radix = 11):
    for i in range(radix):
        buckets = [[] for i in range(radix)]
        for j in lists:
            ## 放入桶 i 中
            buckets[j//(10**i)%10].append(j)
        lists = reduce(add,buckets)
        del buckets
    return lists    


if __name__ == '__main__':
    phone_numbers = [randint(10000000000,99999999999) for num in range(1000000)]
    phone_numbers = radix_sort(phone_numbers)
    #quick_sort(phone_numbers)
    #print(phone_numbers)




