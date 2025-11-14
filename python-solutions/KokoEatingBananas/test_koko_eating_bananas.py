import unittest
from koko_eating_bananas import Solution

class TestKokoEatingBananas(unittest.TestCase):
    
    def setUp(self):
        """Create Solution"""
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.minEatingSpeed([3,6,7,11], 8), 4)
        self.assertEqual(self.solution.minEatingSpeed([30,11,23,4,20], 5), 30)
        self.assertEqual(self.solution.minEatingSpeed([30,11,23,4,20], 6), 23)
    
    def test_edge(self):
        """Test edge cases"""
        self.assertEqual(self.solution.minEatingSpeed([100], 10), 10)
        self.assertEqual(self.solution.minEatingSpeed([1,2,3,4], 100), 1)
        self.assertEqual(self.solution.minEatingSpeed([1,1,1,1,1], 5), 1)

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)