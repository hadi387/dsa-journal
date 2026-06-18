'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

'''

#time complexity -- O(n)
#space -- O(1)



def subarray(nums):
    current_sum = nums[0]
    largest_sum = nums[0]
    for i in nums:
        current_sum = max (current_sum + i, i)
        if current_sum > largest_sum:
            largest_sum = current_sum
    return largest_sum
nums = [1, 2, 3, 0, 6, 0, 9, 4]
result = subarray(nums)
print(result)