# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 08:27:42 2019
@author: Yesser H. Nasser
"""
# Quick sort : recursive divide and conquer sorting algorithm
# Divide and conquer algorithm
# very efficient for large data sets
# worst case is O(n^2)
# Averge case is O(nlogn)
# performance depends largely on pivot selection
def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, low, hi):
    threshold = 20
    if low < hi and hi-low < threshold:
        quick_selection(A, low, hi)
    elif low < hi:
        p = partition(A, low, hi)
        quick_sort2(A, low, p-1)
        quick_sort2(A,p+1, hi)
        
def get_pivot(A, low, hi):
    mid = (hi + low) // 2 
    pivot = hi
    if A[low] < A[mid]:
        if A[mid]<A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = low
    return pivot

def partition (A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low
    
    for i in range(low, hi+1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]
    
    return (border)

def quick_selection(x,first,last):
    for i in range (first, last):
        minIndex = i
        for j in range (i+1, last+1):
            if x[j] < x[minIndex]:
                minIndex = j
        if minIndex != i:
            x[i], x[minIndex] = x[minIndex], x[i]

A = [13,5,6,3,17,41,29,22,54]
print(A)
quick_sort(A)
print(A)

""" Sort a list of 9 integers, we select a pivot. the pivot is the item we use to compare every number to.
move all the number smaller than the pivot to the left and the number bigger than the pivot to the right.
left partition --- pivot ---- right partition
to select pivot we use the median of three method (the median of the first value, the last value and the middle value)

Illustration how the code works (example):
|17| - 41 - 5 - 22 - |54| - 6 - 29 - 3- |13|

=== selection of the pivot ===
the three values are: 17 - 54 - 13 ===> the median is 17
pivot  = 17
41 is border
17 - 41 - 5 - (pivot 17, border = 41, element =5)
is 5 smaller than pivot ===> swap 5 with the border and move both pointers
17 - 5 - 41 - 22 - (pivot 17 , border = 41, element 22)
22 is not smaller than the pivot ===> so we advance to the next element 
17 - 5 - 41 - 22 - 54 - 6 - (pivot 17, border = 41 , element 6) 
6 is smaller than the pivot ===> we swap 6 with border and advance both pointers
17 - 5 - 6 - 22 - 54 - 41 - 29 - 3 - 13 (pivot 17, border = 22, element 29)
29 is not smaller than the pivot ===> we advance to the next element
17 - 5 - 6 - 22 - 54 - 41 - 29 - 3 - 13 (pivot 17, border = 22, element 3)
3 is smaller than pivot ===> swap 3 with border and move both pointers
17 - 5 - 6 - 3 - 54 - 41 - 29 - 22 - 13 (pivot 17, border = 54, element 13)
13 is smaller than pivot ===> swap 13 with border 
17 - 5 - 6 - 3 - 13 - 41 - 29 - 22 - 54 (pivot 17, border = 13) no more element 
we swap 17 with border value

13 - 5 - 6 - 3 - |17| - 41 - 29 - 22 - 54 
All element at left of the pivot are smaller than the pivot

we quick sort to the left partition and quick sort to the right partition
==== The left partition =====:
13 - 5 - 6 -3
median of three
13 - 5 - 3
is 5
we swapt it to the first position
5 is the pivot 
|5| - 13 - 6 - 3 (pivot = 5 , border = 13, element 6)
6 is not smaller than pivot
|5| - 13 - 6 - 3 (pivot = 5 , border = 13, element 3)
3 is smaller than pivot, swap 3 with border. 
|5| - 3 - 6 - 13  (pivot 5, border = 3) no more element swap pivot with border
3 - 5 - 6 - 13 (sorted)
"""

