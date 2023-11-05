#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ this test for edge cases in the max
    funtion
    Args: unittest.Testcase, is a subclass of unittest"""

    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([100, 5, 15, 50, 70]), 100)
        self.assertEqual(max_integer([-8, -9, -15, -4]), -4)
        self.assertEqual(max_integer([70, 70, 70, 70, 70]), 70)
        self.assertEqual(max_integer([-100, 5, 15, -50, -70]), 15)
        with self.assertRaises(TypeError):
            max_integer()
            max_integer(5)
            max_integer((2, 4, 4))

