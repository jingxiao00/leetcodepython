'''
Created on Sep 13, 2018

@author: wangbo
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''

'''learned:
1. Basiclly, all string is composed of assic code, which is 128 in maxium. 
So the trick of ord('/') - ord('a') will still work for assic code.  

'''
import collections

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        
        using hash table
        """
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            elif d[c] is 0:
                d[c] +=1
            else:
                d[c] -=1
        
        if sum(d.values()) in [1,0]:
            return True
        else:
            return False  
                
        
    def canPermutePalindrome2(self, s):
        '''
        using set
        '''
        st = set()
        for c in s:
            if c not in st:
                st.add(c)
            else:
                st.pop(c)
        
        return len(st) in [0,1]
    
    def canPermutePalindrome3(self, s):
        '''
        using ord from assic
        '''
        l = [0] * 128
        for c in s:
            idx = ord(s)
            if l[idx] != 0:
                l[idx]-=1
            else:
                l[idx]+=1        
        return sum(l) in [0,1]
        
