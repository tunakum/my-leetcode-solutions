#input = 5 output = 7, 7 = 111
#input = 10 output = 15, 15 = 1111
#1,3,7,15 ... yani (x * 2) + 1

class Solution(object):
    def smallestNumber(self, n):
        result = 1
        
        while (result <  n):
            result = (result * 2) + 1
        
        return result
            
        
        
        """
        :type n: int
        :rtype: int
        """
        