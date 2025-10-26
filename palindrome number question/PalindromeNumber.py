# x = 121 True
# x = -121 false
# x = 10 false
# x = 1000021

#class Solution(object):
#      def isPalindrome(self, x):
#       """
#       :type x: int
#       :rtype: bool
#       """

#x = input("Enter a number\n")
#print(x[0])
#print(x[len(x) -1 ])

#x = 121021
#print(len(str(x)))
#if (x[i] == x[(len(x) -1) - i]):



def isPalindrome(self,x):
    if (x < 0):
        return False
    
    x = str(x)
    
    for i in range(len(x)):
        if x[i] != x[len(x) - 1 - i]:
            return False
        
    return True
