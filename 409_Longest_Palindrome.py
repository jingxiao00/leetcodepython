'''
Created on Sep 15, 2018

@author: wangbo

Problem:

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

'''Learned:
1. THe counter useage in python:
d = collections.Counter()
for c in s:
    d[c]+=1

is the same as:
d = collections.Counter(s)

2. for i in Counter:

is the same as:
for i in Counter(s).itervalues():

3. python2:
0%3 = 0
1%3 = 1
2%3 = 2
3%3 = 0

0/3=1/3=2/3=0
3/3=4/3=5/3=1
'''

import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        isSingleNumber = False
        d = collections.Counter()
        for c in s:
            d[c]+=1
        
        for c in d:
            ans += d[c]//2
            if d[c]%2 != 0:
                isSingleNumber = True
                
        if isSingleNumber is True:
            return ans*2+1
        else:
            return ans*2
    
                
                
        
                
            
        
        
        
        
        
        
        