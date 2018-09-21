'''
Created on Sep 16, 2018

@author: wangbo

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''


'''What I learned:
1. positive infinite in python: float('inf') and float('-inf'). See:
https://medium.com/@sanatinia/how-to-work-with-infinity-in-python-337fb3987f06

2.Code replace:
a=0
if a < b:
  a=b

is the same as:
a = min(a,b)
    
3. A good way to avoid using the 'inf' is to assign the value as the first number
of the list.

4. 这类题目考的是找一列list中相差最大的数目

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        time complax = O(n)
        space complax = O(1)
        """
        minPrice = float("inf")
        maxProfit = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p-minPrice > maxProfit:
                maxProfit = p-minPrice
            
        return maxProfit
            
            
    def maxProfit2(self, prices):
        '''
        do not use inf
        '''
        minPrice = prices[0]
        maxProfit = 0
        for p in prices[1:]:
            minPrice = min(p, minPrice)
            maxProfit = max(maxProfit, p-minPrice)
                
         
        
        
        
        
        
        
        
        
        
        
