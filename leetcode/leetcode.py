# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         self.x = x
#         if str(x)== str(x)[::-1]:
#             return True
#         else:
#             return False
# r.isPalindrome(121)

#==================================================================================================================================================

# def twosome(arr,target):
#     l,r= 0,len(arr)-1
#     while l<r:
#         current = arr[l]+arr[r]
#         if current == target:
#             return [l,r]
#         elif current < target:
#             l+=1
#         else:
#             r-=1
#     return -1
# arr = [2,7,11,15]
# target = 9
# print(twosome(arr,target))    #it works gives TC - o(n) and SC - o(1) but on sorted array  if array is unsorted two pointer wont work

# def twosome(nums,target):
#     dicti={}
#     n = len(nums)-1
#     for i in range(0,n):
#         remain = target - nums[i]
#         if remain in dicti:
#             return(dicti[remain],i)
#         dicti[nums[i]] = i
#     return -1
# arr=[2,7,11,15]
# target = 9
# print(twosome(arr,target))

#===================================================================================================================================================

