import unittest
from one_bit_two_bit_characters import Solution

class TestOneBitTwoBitCharacters(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.isOneBitCharacter([1,0,0]), True)
        self.assertEqual(self.solution.isOneBitCharacter([1,1,1,0]), False)
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.isOneBitCharacter([0,0,0]), True)
        self.assertEqual(self.solution.isOneBitCharacter([1,1]), False)
        self.assertEqual(self.solution.isOneBitCharacter([1,1,0]), True)

if __name__ == "__main__":
    unittest.main(verbosity = 2)