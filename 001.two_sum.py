'''
Created on Sep 3, 2018

@author: wangbo

1. 暴力方法。
2. hash table用空间换时间。 
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        hash table用空间换时间。2遍pass
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Time:
        Space: 
        """
        a = dict()
        for idx, i in enumerate(nums):
            a[i] = idx
            
        for idx, i in enumerate(nums):
            test = target - i
            if test in a:
                return idx, a[test]
    def twoSum2(self, nums, target):
        """
        hash table用空间换时间，1遍pass
        Time:
        Space:
        """
        a = dict()
        for idx, i in enumerate(nums):
            test = target - i
            if test in a:
                return a[test], idx
            else:
                a[i] = idx
        
if __name__ == '__main__':
    nums = [1,2,3,4,5]
    target = 9
    s = Solution()
    print s.twoSum(nums, target)
    
    