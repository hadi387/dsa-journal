'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English lett
'''
# Approach: Sort both strings and compare. If they're equal, they're anagrams.
# Time complexity - O(n log n)
# Space complexity: O(n)

class validsolution:
    def valid_anagram(self, s, t):
        sorted(s)
        sorted(t)
        if sorted(s) == sorted(t):
            return True
        else:
            return False

solution = validsolution()
result = solution.valid_anagram("house", "lake")
print(result)