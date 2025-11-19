import unittest
from keep_multiplying_found_values_by_two import Solution

class TestKeepMultiplyingFoundValuesByTwo(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
        
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.findFinalValue([1,2,3],4), 4)
        self.assertEqual(self.solution.findFinalValue([2,7,9], 2), 4)
        self.assertEqual(self.solution.findFinalValue([2,4,8,16], 2), 32)
        self.assertEqual(self.solution.findFinalValue([5,3,6,1,12], 3), 24)
        
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.findFinalValue([4], 4), 8)
        self.assertEqual(self.solution.findFinalValue([], 7), 7)
        self.assertEqual(self.solution.findFinalValue([2,4,8,32], 2), 16)
        self.assertEqual(self.solution.findFinalValue([1,1,1,1], 2), 2)

if __name__ == "__main__":
    unittest.main(verbosity = 2)