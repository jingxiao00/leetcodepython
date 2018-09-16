'''
Created on Sep 15, 2018

@author: wangbo

problem:

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
'''

'''Learned
The solution 2 is very beautiful.
'''

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        time complax = O(n)
        space complax = O(n)
        """
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                m=i
        
        n = (1+len(nums))*len(nums)/2 - sum(s)
        
        return [m,n]
    
    def findErrorNums2(self, nums):
        for i in nums:
            if nums[abs(i)-1] < 0:
                m = abs(i)
            else: 
                nums[abs(i)-1] *= -1
            
        for idx, i in enumerate(nums):
            if i > 0:
                n = idx+1
        
        return [m,n]
                
            
        
        
        
        
        
        
        
        
        
         
    