import unittest
from ink.main import main

class TestMain(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(main(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()