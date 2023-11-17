#!/usr/bin/python3
 """ module testbase for base.py"""

import unittest
from models.base import Base


class testbase(unittest.TestCase):
    """ test for the base class """
    def setUp(self):
        self.base1 = Base()
        self.base2 = Base(12)
        self.base3 = Base()

    def test___init__(self):
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 12)
        self.assertEqual(self.base3.id, 2)
