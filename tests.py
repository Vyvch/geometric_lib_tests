import unittest
import random
import math

import circle
import square
import rectangle
import triangle


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(45, 24), 45 * 24)
        self.assertEqual(rectangle.area(40, 29), rectangle.area(29, 40))
        self.assertEqual(rectangle.area(5, 5), 5 * 5)
        self.assertAlmostEqual(rectangle.area(5.5, 3), 5.5 * 3)
        self.assertAlmostEqual(rectangle.area(53535.56767, 3545345.44634), 53535.56767 * 3545345.44634)
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.area(0, 34), 0)
        self.assertEqual(rectangle.area(100 ** 100, 100 ** 10), 100 ** 110)
        self.assertEqual(rectangle.area(4535245354, 453453452345359), 4535245354 * 453453452345359)
        for _ in range(1000):
            a, b = random.randint(0, 10000000000), random.randint(0, 10000000000)
            self.assertEqual(rectangle.area(a, b), a * b)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(45, 24), 2 * (45 + 24))
        self.assertEqual(rectangle.perimeter(40, 29), rectangle.perimeter(29, 40))
        self.assertEqual(rectangle.perimeter(5, 5), 2 * (5 + 5))
        self.assertAlmostEqual(rectangle.perimeter(5.5, 3), 2 * (5.5 + 3))
        self.assertAlmostEqual(rectangle.perimeter(53535.56767, 3545345.44634), 2 * (53535.56767 + 3545345.44634))
        self.assertEqual(rectangle.perimeter(10, 0), 2 * (10 + 0))
        self.assertEqual(rectangle.perimeter(0, 34), 2 * (0 + 34))
        self.assertEqual(rectangle.perimeter(100 ** 100, 100 ** 10), 2 * (100 ** 100 + 100 ** 10))
        self.assertEqual(rectangle.perimeter(4535245354, 453453452345359), 2 * (4535245354 + 453453452345359))
        for _ in range(1000):
            a, b = random.randint(0, 10000000000), random.randint(0, 10000000000)
            self.assertEqual(rectangle.perimeter(a, b), 2 * (a + b))
        

class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(square.area(5), 5 ** 2)
        self.assertEqual(square.area(0), 0)
        self.assertAlmostEqual(square.area(2.5), 2.5 ** 2)
        self.assertEqual(square.area(10 ** 10), (10 ** 10) ** 2)
        self.assertEqual(square.area(3 ** 345345), (3 ** 345345) ** 2)
        self.assertEqual(square.area(44553453462366563466), 44553453462366563466 ** 2)
        self.assertAlmostEqual(square.area(5353453.3453453453), 5353453.3453453453 ** 2)
        for _ in range(1000):
            a = random.randint(0, 10000000000)
            self.assertEqual(square.area(a), a ** 2)

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(5), 4 * 5)
        self.assertEqual(square.perimeter(0), 0)
        self.assertAlmostEqual(square.perimeter(2.5), 4 * 2.5)
        self.assertEqual(square.perimeter(10 ** 10), 4 * (10 ** 10))
        self.assertEqual(square.perimeter(3 ** 345345), 4 * (3 ** 345345))
        self.assertEqual(square.perimeter(44553453462366563466), 4 * 44553453462366563466)
        self.assertAlmostEqual(square.perimeter(5353453.3453453453), 4 * 5353453.3453453453)
        for _ in range(1000):
            a = random.randint(0, 10000000000)
            self.assertEqual(square.perimeter(a), 4 * a)
        
        
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        self.assertAlmostEqual(triangle.area(10, 4), 0.5 * 10 * 4)
        self.assertAlmostEqual(triangle.area(345, 123), triangle.area(123, 345))
        self.assertAlmostEqual(triangle.area(2534, 0), 0)
        self.assertAlmostEqual(triangle.area(2.5, 3.5), 0.5 * 2.5 * 3.5)
        self.assertAlmostEqual(triangle.area(100 ** 20, 100), 0.5 * (100 ** 20) * 100)
        self.assertAlmostEqual(triangle.area(345, 33), 0.5 * 345 * 33)
        self.assertAlmostEqual(triangle.area(445534534623, 453465636), 0.5 * 445534534623 * 453465636)
        self.assertAlmostEqual(triangle.area(5353453.3453453453, 654325.5737), 0.5 * 5353453.3453453453 * 654325.5737)
        for _ in range(1000):
            a, b = random.randint(0, 10000000000), random.randint(0, 10000000000)
            self.assertAlmostEqual(triangle.area(a, b), 0.5 * a * b)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 3 + 4 + 5)
        self.assertEqual(triangle.perimeter(234, 52, 69), triangle.perimeter(52, 69, 234))
        self.assertAlmostEqual(triangle.perimeter(2.5, 3.5, 4.5), 2.5 + 3.5 + 4.5)
        self.assertEqual(triangle.perimeter(100 ** 10, 100 ** 5, 100 ** 2), 100 ** 10 + 100 ** 5 + 100 ** 2)
        self.assertEqual(triangle.perimeter(35324545, 546456456, 454625246), 35324545 + 546456456 + 454625246)
        self.assertAlmostEqual(triangle.perimeter(6465436.346546, 848362654537.34585, 348569478357.366536),
                                                6465436.346546 + 848362654537.34585 + 348569478357.366536)
        for _ in range(1000):
            a, b, c = random.randint(0, 10000000000), random.randint(0, 10000000000), random.randint(0, 10000000000)
            self.assertEqual(triangle.perimeter(a, b, c), a + b + c)
        
        
class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(1), math.pi)
        self.assertAlmostEqual(circle.area(0), 0)
        self.assertAlmostEqual(circle.area(43545), math.pi * (43545 ** 2))
        self.assertAlmostEqual(circle.area(2.5), math.pi * (2.5 ** 2))
        self.assertAlmostEqual(circle.area(134.6), math.pi * (134.6 ** 2))
        self.assertAlmostEqual(circle.area(10 ** 10), math.pi * ((10 ** 10) ** 2))
        self.assertAlmostEqual(circle.area(3454534), math.pi * (3454534 ** 2))
        self.assertAlmostEqual(circle.area(345435.6456), math.pi * (345435.6456 ** 2))
        for _ in range(1000):
            a = random.randint(0, 1000)
            self.assertAlmostEqual(circle.area(a), math.pi * (a ** 2))

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle.perimeter(0), 0)
        self.assertAlmostEqual(circle.perimeter(43545), 2 * math.pi * 43545)
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5)
        self.assertAlmostEqual(circle.perimeter(134.6), 2 * math.pi * 134.6)
        self.assertAlmostEqual(circle.perimeter(10 ** 10), 2 * math.pi * (10 ** 10))
        self.assertAlmostEqual(circle.perimeter(66546365463547356), 2 * math.pi * 66546365463547356)
        self.assertAlmostEqual(circle.perimeter(345435.6456346), 2 * math.pi * 345435.6456346)
        for _ in range(1000):
            a = random.randint(0, 1000)
            self.assertAlmostEqual(circle.perimeter(a), 2 * math.pi * a)