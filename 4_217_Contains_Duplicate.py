'''
Created on Sep 5, 2018

@author: wangbo
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False 
            
            
            