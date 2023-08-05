import unittest
from localc.scanner import *


class TestScanner(unittest.TestCase):
    def test_scanning(self):
        s = "true and false"
        self.assertEqual(scan(s), ['true', 'and', 'false'])

        s = "(true and false) or true"
        self.assertEqual(scan(s), ['(', 'true', 'and', 'false', ')', 'or', 'true'])


if __name__ == '__main__':
    unittest.main()
