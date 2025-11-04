#mantık olarak left right ı doğru kurdum ama aktarabilmem çok uzun sürdü sorunun discussion kısmındaki hintlerden yararlanarak çözdüm

class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        product = 1
        for i in range(len(nums)):
            answer[i] = product
            product *= nums[i]

        product = 1
        for i in reversed(range(len(nums))):
            answer[i] *= product
            product *= nums[i]

        return answer         
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        