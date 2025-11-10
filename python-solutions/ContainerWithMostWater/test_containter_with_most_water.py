import unittest
from container_with_most_water import Solution

class TestContainerWithMostWater(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
    
    def test_basic_cases(self):
        """Test basic cases"""
        self.assertEqual(self.solution.maxArea([1,8,6,2,5,4,8,3,7]), 49)
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.maxArea([1,1]), 1)
        self.assertEqual(self.solution.maxArea([10]), 0)
        self.assertEqual(self.solution.maxArea([5,5,5,5]), 15)

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)