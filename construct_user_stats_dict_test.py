#!/usr/bin/env python3

import unittest
from ticky_check import contruct_user_stats_dict


class ConUserStatsDictTest(unittest.TestCase):

    def test_basic(self):
        testcase1 = ["ERROR", "ERROR", "INFO"]
        testcase2 = ["user_D", "user_S", "user_D"]
        expected = {"user_D": [1, 1], "user_S": [0, 1]}
        self.assertEqual(contruct_user_stats_dict(testcase1, testcase2), expected)

    def test_empty(self):
        testcase1 = []
        testcase2 = []
        self.assertRaises(AssertionError, contruct_user_stats_dict, testcase1, testcase2)

    def test_no_user(self):
        testcase1 = ["INFO", "ERROR"]
        testcase2 = []
        self.assertRaises(AssertionError, contruct_user_stats_dict, testcase1, testcase2)

    def test_no_log_type(self):
        testcase1 = []
        testcase2 = ["user_D", "user_S"]
        self.assertRaises(AssertionError, contruct_user_stats_dict, testcase1, testcase2)

    def test_diff_num(self):
        testcase1 = ["INFO", "ERROR", "INFO"]
        testcase2 = ["user_D", "user_S"]
        self.assertRaises(AssertionError, contruct_user_stats_dict, testcase1, testcase2)


if __name__ == "__main__":
    unittest.main()
