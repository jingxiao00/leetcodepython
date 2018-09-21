'''
Created on Sep 16, 2018

@author: wangbo

problem:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i in range(len(nums)):
            if nums[i] is 0:
                zeros+=1
            else:
                if zeros is not 0:
                    nums[i-zeros] = nums[i]
                    nums[i] = 0
        return nums
                    
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    s = Solution()
    print s.moveZeroes(nums)
                
        