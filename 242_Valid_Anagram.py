'''
Created on Sep 13, 2018

@author: wangbo

Problem:
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

"""
Learned:
1. The string type problem has a very common solution pattern is to use ord to 
convert the string to a list counter. Another very common solution is to use 
hash table to count. 
 
2. Note that the space complaxity is: O(1)

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Solution: Use ord to convert character of the string into number, 
        use a list to build the number count. 
        """
        c1 = [0]*26
        c2 = [0]*26
        
        for c in s:
            c1[ord(c)-ord('a')] += 1
        for c in t:
            c2[ord(c)-ord('a')] += 1
            
        for i,j in zip(c1, c2):
            if i!=j: 
                return False
        return True
        
    def isAnagram(self, s, t):
        """
        Use hash table
        """
        d1 = {}
        
        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        
        for c in t:
            if c in d1:
                d1[c] -= 1
            else:
                return False     
        
        for k in d1:
            if d1[k] != 0:
                return False
        return True
            
            
        
        