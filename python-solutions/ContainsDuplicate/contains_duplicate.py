# [1,2,3,1] true
# [1,2,3,4] false

class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
            
        """
        :type nums: List[int]
        :rtype: bool
        """
        