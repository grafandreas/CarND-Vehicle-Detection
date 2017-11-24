import unittest
import class_load
import sys


class TestStringMethods(unittest.TestCase):

    def test_load(self):
        print(sys.version)
        (cars, nocars) = class_load.load()
        self.assertEqual(8792, len(cars))
        self.assertEqual(8968, len(nocars))

if __name__ == '__main__':
    unittest.main()