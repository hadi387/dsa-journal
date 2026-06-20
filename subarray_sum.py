'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
# Time complexity -- O(n)
# Space complexity -- O(n)
def subarraySum(nums, k) -> int:
    count = 0
    current = 0
    seen = {0: 1}  # before array starts, sum is 0

    for n in nums:
        current += n
        if current - k in seen:
            count += seen[current - k]
            seen[current] = seen.get(current, 0) + 1

    return count
        