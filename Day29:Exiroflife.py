'''Flamel is making the Elixir of Life but he is missing a secret ingredient,
a set of contiguous plants (substring) from the Garden of Eden.The garden consists of various plants represented by
string S where each letter represents a different plant. But the prophecy has predicted that the correct set of plants
required to make the potion will appear in the same contiguous pattern (substring) at the beginning of the forest (prefix),
the end of the forest (suffix), and will also be the most frequent sequence present in the entire forest.
Identify the substring of plants required to make the elixir and find out the number of times it appears in the forest. 

Example 1:

Input: S = "ababaaaab"
Output: 3
Explanation: substring "ab" is a prefix, 
a suffix and appears 3 times.

Example 2:

Input: S = "aaaa"
Output: 4
Explanation: substring "aaaa" occurs 1 time, 
substring "aaa" occurs 2 times, substring 
"aa" occurs 3 times, substring "a" occurs 
4 times. All of them are proper prefixes 
and suffixes. But, "a" has the maximum 
frequency.
Example 3:

Input: S = "abcdef"
Output: 1'''
#Solution1
class Solution:
    def maxFrequency(self, s):
        n = len(s) 
        s1 ="" 
        for i in s:
            if i not in s1:
                s1 += i 
        if s1 == s:
            return 1
            
        temp = ""
        for i in range(1,n):
            if s[:i] == s[n-i:n]:
                temp = s[:i]
                break
            else:
                temp = s
        c = s.count(temp)
        return c
