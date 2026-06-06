'''Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that:

Each input has exactly one solution.
You may not use the same element twice.
You can return the answer in any order.
Example 1
Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9
Example 2
Input:
nums = [3,2,4]
target = 6

Output:
[1,2]
Example 3
Input:
nums = [3,3]
target = 6

Output:
[0,1]
Constraints
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
Follow-up

Can you come up with an algorithm that runs in less than O(n²) time complexity? '''


class Solution:
    def twoSum (nums, target):
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return[seen[needed], i]
            seen [nums[i]] = i
            print(seen)
            

    nums = [2, 3, 4]
    print(twoSum(nums, 6))

