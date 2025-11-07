import unittest
from valid_palindrome import Solution
class TestValidPalindrome(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.isPalindrome("a"), True)
        self.assertEqual(self.solution.isPalindrome("aa"), True)
        self.assertEqual(self.solution.isPalindrome("ab"), False)
        self.assertEqual(self.solution.isPalindrome("A man, a plan, a canal: Panama"), True)
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.isPalindrome(""), True)
        self.assertEqual(self.solution.isPalindrome(" "), True)
        self.assertEqual(self.solution.isPalindrome("!@#$"), True)
        self.assertEqual(self.solution.isPalindrome("ab_a"), True)
        self.assertEqual(self.solution.isPalindrome("0P"), False)

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)
        