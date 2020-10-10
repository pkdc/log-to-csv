#!/usr/bin/env python3

import unittest
from ticky_check import construct_error_dict


class ConErrDictTest(unittest.TestCase):

    def test_basic(self):
        testcase = ["Connection to DBS failed",
                    "Connection to DB failed", "Connection to DBS failed"]
        expected = {"Connection to DBS failed": 2, "Connection to DB failed": 1}
        self.assertEqual(construct_error_dict(testcase), expected)

    def test_empty(self):
        testcase = []
        self.assertRaises(ValueError, construct_error_dict, testcase)


if __name__ == "__main__":
    unittest.main()
