# arr1 = [1,2,3,4,5,6,7,8]
# print(arr1[::-1])

# #swapping----------------------------------------------------------------
# def swap(arr,i,j):
     
#     arr[i],arr[j] = arr[j],arr[i]
#     return arr

# print(swap([10,20,30,40],0,2))

# #Access & indexing------------------------------------------------------
# arr = [10,20,30,40,50]
# print(arr[0],arr[-1],arr[-2])

# # print(arr[-2:])
# # print(arr[:1])

# arr = [10,20,30,40,50]
# arr[2]= 99
# print(arr)


# # slicing

# arr = [1,2,3,4,5,6,7,8,9]
# print(arr[:3])
# print(arr[-3:])
# print(arr[1:len(arr)-1])
# print(arr[::-1])
# print(arr[::2])

# arrr = [5,10,15,20]
# for i,j in enumerate(arrr):
#     print(i,j)

# print('even only')

# for i,j in enumerate(arrr):
#     if i%2 == 0:
#         print(i,j)


# def addition(arr1,arr2):
#    for i,j in zip(arr1,arr2):
#        print(i,j)

# arr1 = [1,2,3,4]
# arr2 = ['x','y','z']
# addition(arr1,arr2)
# print(addition)

# #swapping 
# def swap(arr,a,b):
#     arr[a],arr[b] = arr[b],arr[a]
#     return arr

# arr = [10,20,30,40,50]
# print(swap(arr,0,3))


# def twoPointer_reverse(arr):
#     l,r = 0,len(arr)-1
#     while l< r:
#         arr[l],arr[r] = arr[r],arr[l]
#         l+=1
#         r-=1
#     return arr

# arr = [1,2,3,4,5]
# print(twoPointer_reverse(arr))


#palindrome 

# a = 'level'
# if a == a[::-1]:
#     print('palindrome')
# else:
#      print('Not')


# def palindrome_twosome(arr):
#     l,r = 0,len(arr)-1
#     while l < r:
#         if arr[l] != arr[r]:
#          return False
#         l += 1
#         r -= 1
#     return True

# print(palindrome_twosome('level'))

def move_zeroes(arr):
    write = 0

    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1

    return arr
print(move_zeroes([1,5,0,4,7,2,0]))