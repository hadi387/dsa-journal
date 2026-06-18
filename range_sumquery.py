'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.
'''
# Approach: Build a prefix sum array upfront. Each position stores the sum 
# of all elements from the start up to that point.
# To get sum between left and right: prefix[right] - prefix[left-1]
# Time Complexity: O(n) to build, O(1) per query
# Space Complexity: O(n) for the prefix array

nums = [-2, 0, 3, -5, 2, -1]

prefix = []
total = 0

for n in nums:
    total += n
    prefix.append(total)

def sumRange(left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]

print(sumRange(0, 2))
print(sumRange(2, 5))
print(sumRange(0, 5))