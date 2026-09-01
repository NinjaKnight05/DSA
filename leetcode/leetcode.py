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

# def remove_duplicates(nums):
#     l,r=0,1
#     while r< len(nums):
#         if nums[l]!=nums[r]:
#             l+=1
#             nums[l] = nums[r]
#         r+=1
#     return l+1
# nums = [1,1,2,2,3,3,4]
# print(remove_duplicates(nums))

# ===================================================================================================================================================
# def plusOne(nums):
#     for i in nums:
#         if i == len(nums)-1:
#             nums[i]+=1
#             return nums
#     return None
# nums = [4,3,2,1]
# print(plusOne(nums))

# def plusOne(nums):
#     for i in range(len(nums)-1,-1,-1):
#         if nums[i]==9:
#             nums[i]=0
#         else:
#             nums[i]+=1
#             return nums
#     nums.insert(0,1)
#     return nums
# nums = [9]
# print(plusOne(nums))

# def addition(nums):
#     nums = int("".join(map(str,nums)))
#     nums+=1
#     return list(map(int, str(abs(nums))))
# nums = [9]
# print(addition(nums))

#========================================================================================================================================================


