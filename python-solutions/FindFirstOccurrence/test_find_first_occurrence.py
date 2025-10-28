import unittest
from find_first_occurrence import Solution

class TestFindFirstOccurence(unittest.TestCase):
    
    def setUp(self):
        """Create solution before test"""
        self.solution = Solution()
    
    def test_basic(self):
        """Basic test found needle"""
        result = self.solution.strStr("sadbutsad", "sad")
        self.assertEqual(result,0)
    
    def test_not_found(self):
        """Needle not found"""
        result = self.solution.strStr("leetcode", "leeto")
        self.assertEqual(result,-1)
    
if (__name__ == "__main__"):
    unittest.main()