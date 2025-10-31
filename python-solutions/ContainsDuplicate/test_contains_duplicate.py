import unittest
from contains_duplicate import Solution

class TestContainsDuplicate(unittest.TestCase):

    def setUp(self):
        """Create solution before test"""
        self.solution = Solution()
    
    def test_basic(self):
        """Test contains duplicate"""
        self.assertEqual(self.solution.containsDuplicate([1,2,3,1]), True)
        self.assertEqual(self.solution.containsDuplicate([1,2,3,2,4,3]), True)
        self.assertEqual(self.solution.containsDuplicate([1,1,2]), True)
        self.assertEqual(self.solution.containsDuplicate([1,2,3,3]), True)
        
    def test_not_found(self):
        """Test does not contain duplicate"""
        self.assertEqual(self.solution.containsDuplicate([1,2,3,4]), False)
        self.assertEqual(self.solution.containsDuplicate([3,4,5,6]), False)
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.containsDuplicate([]), False)
        self.assertEqual(self.solution.containsDuplicate([2]), False)
        self.assertEqual(self.solution.containsDuplicate([1,1,1,1,1]), True)
        
if (__name__ == "__main__"):
    unittest.main(verbosity = 2)
