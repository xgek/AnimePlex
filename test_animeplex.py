# test_animeplex.py
"""
Tests for AnimePlex module.
"""

import unittest
from animeplex import AnimePlex

class TestAnimePlex(unittest.TestCase):
    """Test cases for AnimePlex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimePlex()
        self.assertIsInstance(instance, AnimePlex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimePlex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
