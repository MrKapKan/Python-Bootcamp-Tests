import unittest
from hash_string import hash_func


class TestHashFunc(unittest.TestCase):

    def test_hash(self):
        self.assertEqual(hash_func('Python Bootcamp'), '5f312b1622f97b5f6cc6652087c604803faf4a2d')


if __name__ == "__main__":
    unittest.main()
