#class Solution(object):
 #   def romanToInt(self, s):
  #      """
   #     :type s: str
    #    :rtype: int
     #   """
#I V den X ten önce gelebilir
# X L ve C den
#C D ve M den
        
def romanToInt(s):
    
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    
    all = 0
    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            all -= roman[s[i]]
        else:
            all +=roman[s[i]]
    
    return all

        