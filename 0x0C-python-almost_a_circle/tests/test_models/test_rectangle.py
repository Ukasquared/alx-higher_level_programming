#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
      self.r1 = Rectangle(10, 2)
      self.r4 = Rectangle(4, 5, 6, 18, 2)

    def test__init__(self):
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r4.width, 4)
        self.assertEqual(self.r4.height, 5)
        self.assertEqual(self.r4.id, 2)
        self.assertEqual(self.r4.y, 18)
        self.assertEqual(self.r4.x, 6)

        with self.assertRaises(TypeError):
            Rectangle(None, None)
            Rectangle(5, None)
            Rectangle(5, 8, -1)
            Rectangle()
            Rectangle([], {}, -1, '5')
            self.r5 = Rectangle(5, 8, -1)

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r4.area(), 20)

    def test__str(self):
        result = self.r1.__str__()
        self.assertEqual(result, "[Rectangle] (1) 0/0 - 10/2")

    def test__str(self):
        result_t = self.r4.__str__()
        self.assertEqual(result_t, "[Rectangle] (2) 6/18 - 4/5")

    def test_update(self):
        self.r1.update(5, 15, 4)
        result = self.r1.__str__()
        self.assertEqual(result, "[Rectangle] (5) 0/0 - 15/4")

    def test_update(self):
        self.r4.update(width=7, y=5, x=10, height=7)
        result_t = self.r4.__str__()
        self.assertEqual(result_t, "[Rectangle] (2) 10/5 - 7/7")
