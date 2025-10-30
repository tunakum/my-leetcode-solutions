# sqrt(8) = 2.82842..... -> sqrt(8) = 2
#sqrt(4) = 2 
# sqrt(16) = 16 - 1, 15 - 3, 12 - 5, 7-7, = 0 4 kere işlem yapıldı cevap 4
class Solution(object):
    def mySqrt(self, x):
        counter = 0
        odd_number = 1
        while(x > 0):
            x -= odd_number
            odd_number+= 2
            counter+=1
        if (x < 0):
            counter -= 1
            return counter
        return counter
        
    """
    :type x: int
    :rtype: int
    """