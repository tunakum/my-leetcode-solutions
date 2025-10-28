# haystack = "apple" needle = "ap" olduğunda output 0 olacak
# haystack = "apple" needle ="sad" olduğunda output -1 olacak
# haystack içerisinde needle arayıp başladığı indexi output olarak verilecek 

                    
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if (haystack[i: i+len(needle)] == needle):
                return i
        return -1       
        
                
  #      """
   #     :type haystack: str
    #    :type needle: str
     #   :rtype: int
      #  """
        