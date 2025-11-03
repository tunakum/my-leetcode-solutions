import unittest
from top_k_frequent_elements import Solution

class TestTopFrequentElements(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic"""
        self.assertEqual(self.solution.topKFrequent([1,1,1,2,2,3],2), [1,2])
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.topKFrequent([3],1), [3])
        self.assertEqual(self.solution.topKFrequent([4,4,4,4], [1]), [4])
        
        
if __name__ == "__main__":
    unittest.main(verbosity = 2)