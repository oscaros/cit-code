'''
1. Using a while loop, implement bubble sort algorithm
2. Using a while loop, implement selection sort algorithm
'''

#1 bubble osrt
#get first item
#get next item
#compare the two
#if 1st item is less that second item, swap the two and go to next item

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for y in range(n-i-1):
            if arr[y] > arr[y+1]:
                arr[y],arr[y+1] = arr[y+1], arr[y]
    return arr


print(bubble_sort([2,7,5,8]))

#with while loop
def bubble_sort2(arr):
    for i in range(len(arr)):
        j=0
        while j < len(arr)-1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j=j+1
        
    return arr

print(bubble_sort2([2,7,5,8]))

def bubbleSort3(l):
    i = 0
    while i<len(l):
        j = 0
        while j<len(l)-1:
            if l[j+1] < l[j]:
                l[j], l[j+1] = l[j+1], l[j]
            j += 1
        i += 1
    return l

# print(bubbleSort3([8,3,4,6,9,3,5,7,4]))





