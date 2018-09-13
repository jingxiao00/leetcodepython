'''
Created on Sep 13, 2018

@author: wangbo

Problem: 
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

 
Learned:
1. A balk code to one line of code:
s = set()
for i in nums:
    s.add(i)

is the same as s = set(nums)


2.Consider: what is the complaxicty to iterator through a dict/set?: 
Answer: 
a set/dict do not hve order, to iter through it is the same as: 
set.pop() until there is no items. The complaxity shoud be n, which is the length
of the dict/set

'''

class Solution(object):
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Use math. 
        """
        s = set()
        summ = 0
        for i in nums:
            if i not in s:
                s.add(i)
                summ+=i
            else:
                s.remove(i)
                summ-=i
        return summ
                
    def singleNumber2(self, nums):
        s = set()
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                s.remove(n)
                
        return s.pop()
        
        
                 
        
        
        