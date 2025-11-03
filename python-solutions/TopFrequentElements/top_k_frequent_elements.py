from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        most_common = count.most_common(k)
        
        result = []
        
        for i in most_common:
            result.append(i[0])
        return result
                    
        
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        