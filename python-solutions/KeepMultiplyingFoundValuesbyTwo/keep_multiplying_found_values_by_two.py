class Solution(object):
    def findFinalValue(self, nums, original):
        nums = sorted(nums)
        
        if original not in nums:
            return original
        
        while original in nums:
            original *= 2
            
        return original
        

        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        