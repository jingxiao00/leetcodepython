'''
Created on Sep 4, 2018
@author: wangbo
* 注意corner cases: 输入为 ""， 或者" ", 题目出现之后首先要写出corner case.
'''

class SLS(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
                利用set来做检查
        """
        longest = 1
        s1 = set()
        l1 = list()
        for i in s:
            if i not in s1:
                s1.add(i)
                l1.append(i)
            else:
                if len(s1) > longest:
                    longest  = len(s1)
                for idx, j in enumerate(l1):
                    if j == i:
                        l1 = l1[idx+1:]
                        l1.append(i)
                        s1 = set(l1)
        return longest
                
    def lengthOfLongestSubstring2(self, s):
        """
                利用dict 来储存idx
        """
        ans = 0
        anchor = 0
        d1 = dict()
        for idx, i in enumerate(s):
            if i in d1:
                anchor = max(anchor, d1[i]+1)
                ans = max(ans, idx-anchor+1)
            else:
                ans = max(ans, idx-anchor+1)
            d1[i] = idx

        if ans == 0:
            return len(s)
        else:
            return ans
    
            
            
            
        