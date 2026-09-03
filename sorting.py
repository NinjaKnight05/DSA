# #shallow copy and deep copy

# print('shallow copy')
# orignal = [[1,2] , [3,4]]
# shallow_copy = orignal.copy()
# shallow_copy [0][0] = 999

# print(shallow_copy)
# print(orignal)

# print("------------------------------------------------")
# print('deep copy')

# orignal1 = [[1,2] , [3,4]]
# import copy
# deep_copy = copy.deepcopy(orignal)
# deep_copy[0][0] = 888

# print(orignal1)
# print(deep_copy)


#sorting
# def bubble_Sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j] < arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 swapped = True
#         if not swapped:
#          break
#     return arr
# arr = [1,3,5,4,6,2,8]
# print(bubble_Sort(arr))

