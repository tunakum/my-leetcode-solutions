import unittest
from longest_consecutive_sequence import Solution

class TestLongestConsecutiveSequence(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.longestConsecutive([1,2,0,1]), 3)
        self.assertEqual(self.solution.longestConsecutive([100,4,200,1,3,2]), 4)
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.longestConsecutive([]), 0)
        self.assertEqual(self.solution.longestConsecutive([3]), 1)
        self.assertEqual(self.solution.longestConsecutive([0,-1,-2,-3]), 4)
        self.assertEqual(self.solution.longestConsecutive([2,2,2]), 1)

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)