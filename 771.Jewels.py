'''
Created on Sep 4, 2018

@author: wangbo

'''

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d = dict()
        for i in S:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        answer = 0
        for j in J:
            answer += d.get(j,0)
        return answer
    
    def numJewelsInStones2(self, J, S):
        """
        for each stone check if it is a jewels.
        """
        J = set(J)
        answer = 0
        for s in S:
            if s in J:
                answer +=1
        return answer
        
        
        
            