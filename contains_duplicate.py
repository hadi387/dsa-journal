'''
Problem Statement

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1
Input:
nums = [1,2,3,1]

Output:
true

Explanation:
The element 1 appears more than once.
Example 2
Input:
nums = [1,2,3,4]

Output:
false

Explanation:
All elements are unique.
Example 3
Input:
nums = [1,1,1,3,3,4,3,2,4,2]

Output:
true
Constraints
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
Follow-up

Can you solve the problem in O(n) time complexity?
'''

# Approach: Store seen numbers in a dictionary.
# If we see a number already in the dictionary, return True.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Duplicate:
    def containsduplicate(nums):
        seen = set()
        print (seen)
        for num in nums:
            print(num)
            print(seen)
            if num in seen:
                print(num)
                return True
         
            seen.add(num)
            print(seen)

        return False
       
    
    nums = [1,2,3,4,1]
    is_true = containsduplicate(nums)
    print(is_true)

