#!/usr/bin/python3

import unittest
from models import Rectangle  # Adjust based on your actual file structure


class TestRectangle(unittest.TestCase):


    def test_area_calculation(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)


    def test_width_update(self):
        rect = Rectangle(4, 5)
        rect.width = 8
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.area(), 40)


if __name__ == '__main__':
    unittest.main()
