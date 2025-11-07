#searched information about "remove all the spaces and other chars"
import re
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return s == s[::-1]

        """
        :type s: str
        :rtype: bool
        """
        