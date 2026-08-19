# Linear search
def linear_search(arr,target):
    for i in range(0,len(arr)-1):
        if arr[i] == target:
            return i
    return -1
arr = [27,13,45,20,32]
print(linear_search(arr,20))


def linear_search(arr,target):
    for i,j in enumerate(arr):
        if j == target:
            return i
    return -1
arr = [27,13,45,20,32]
print(linear_search(arr,20))
 
# Binary Search
def binary_search(arr,target):
    left,right = 0, (len(arr)-1)
    while left < right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

arr = [10,20,30,40,50,60,70,80,90,100]
print(binary_search(arr,100))

