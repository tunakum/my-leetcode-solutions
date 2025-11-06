# My first solution worked logically but wasn't O(n), so I improved it to an optimal solution using a hash set.
class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            if(num - 1 not in num_set):
                length = 1
                current = num
                
                while(current + 1 in num_set):
                    current += 1
                    length += 1

                longest = max(longest, length)
        
        return longest
        """
        :type nums: List[int]
        :rtype: int
        """
        