'''
Created on Sep 12, 2018

@author: wangbo

Problem: Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.


Learned:
1. how to use ord to convert a character to number. 
2. how to crate a dict with list as initial value from python 'collections'.  
'''

import collections 

class Solution(object):
    def groupAnagramS1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        We sort each str and used it as key in a dict.
        time complax: n*Llog(L) 
        space complax: n*L 
        """
        ans = []
        groups = {}
        
        for str in strs:
            sortedStr = ''.join(sorted(str)) 
            if sortedStr not in groups:
                groups[sortedStr]=[str]
            else:
                groups[sortedStr].append(str)
        
        for k in groups:
            ans.append(groups[k])
        
        return ans
    
    def groupAnagramS2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        We sort each str and used it as key in a dict.
        time complax: n*Llog(L) 
        space complax: n*L 
        """
        d = collections.defaultdict(list)
        for str in strs:
            k = [0]*26
            for c in str:
                k[ord(c) - ord('a')]+=1
            d[tuple(k)].append(str)
                
        return d.values()
                    
                
                
            
            
                    
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print s.groupAnagramS1(strs)
    print s.groupAnagramS2(strs)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        