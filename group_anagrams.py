'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

'''

class Solution:
    def groupanagrams (str):
        strs_stores = {}
        for i in str:
            key = "".join(sorted(i))
            if key not in strs_stores:
                strs_stores[key] = []
            strs_stores[key].append(i)
        return list (strs_stores.values())

print(Solution.groupanagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
print(Solution.groupanagrams(["x"]))
print(Solution.groupanagrams([""]))