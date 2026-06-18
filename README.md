What I Learned

Hash Maps
A hash map is basically a dictionary. You use it to store keys and values.
I use it when I need to remember how many times I've seen an element,
or to group items that share something in common.

Patterns

Track min/max in one pass
Used in: Best Time to Buy and Sell Stock
Keep two variables as you loop — update them when you find something better.

Sort to group similar items
Used in: Group Anagrams
Sort each word's letters to create a key. Words with the same key are anagrams.

Count frequencies
Used in: Valid Anagram, Top K Frequent Elements, Contains Duplicate
Use a dictionary to count how many times each element appears.

Kadane's Algorithm
Used in: Maximum Subarray
At each number, decide: add it to current sum or start fresh? Track the best sum seen.

Prefix Sum
Used in: Range Sum Query
Build a running total array upfront. Subtract prefix values to get sum between two positions instantly.

Problems Solved

Two Sum — Easy — O(n²) time, O(1) space
Contains Duplicate — Easy — O(n) time, O(n) space
Best Time to Buy and Sell Stock — Easy — O(n) time, O(1) space
Valid Anagram — Easy — O(n log n) time, O(n) space
Group Anagrams — Medium — O(n * k log k) time, O(n) space
Top K Frequent Elements — Medium — O(n log n) time, O(n) space
Longest Consecutive Sequence — Medium — O(n) time, O(n) space
Valid Palindrome — Easy — O(n) time, O(n) space
Maximum Subarray — Medium — O(n) time, O(1) space
Range Sum Query — Easy — O(n) build, O(1) query, O(n) space