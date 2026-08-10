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
