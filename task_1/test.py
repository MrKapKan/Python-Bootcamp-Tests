import unittest
from hash_string import hash_func


class TestHashFunc(unittest.TestCase):

    def test_hash(self):
        self.assertEqual(hash_func('Hello World'), '0a4d55a8d778e5022fab701977c5d840bbc486d0')


if __name__ == "__main__":
    unittest.main()
