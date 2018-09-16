'''
Created on Sep 15, 2018

@author: wangbo

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
'''

'''learned:
online solution:

def areSentencesSimilar(self, words1, words2, pairs):
    if len(words1) != len(words2):
    s = set(map(tuple, pairs))
    return all((i,j) in set or (j,i) in s or i==j for i,j in zip(words1,words2))
'''

import collections
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        
        m = len(pairs)
        n = len(words)
        time complex = O(m+n)
        space complex = O(m)
        """
        if len(words1) != len(words2):
            return False
        
        if len(words1) is 0 and len(words2) is 0:
            return True
        
        d = collections.defaultdict(set)
        for i,j in pairs:
            d[i].add(i)
            d[j].add(j)
        
        for i,j in zip(words1, words2):
            if i==j:
                continue
            if j not in d[i]:
                return False
        
        return True
    
            
        
            
        
        
        
        
        
        
        
        
        
        
        