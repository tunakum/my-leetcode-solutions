import unittest
from two_sum_2 import Solution

class TestTwoSum2(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.twoSum([2,7,11,15], 9), [1,2])
        self.assertEqual(self.solution.twoSum([2,3,4], 6), [1,3])

    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.twoSum([1,2], 3), [1,2])
        self.assertEqual(self.solution.twoSum([-5,-3,0,4,10], -8), [1,2])
        self.assertEqual(self.solution.twoSum([1,3,3,4], 6), [2,3])
    
if(__name__ == "__main__"):
    unittest.main(verbosity = 2)