import unittest

class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5+5, 10)
        self.assertEqual(5+6, 11)
    
    def test_kamil(self):
        kamil = "głodny"
        self.assertEqual(kamil, "głodny")