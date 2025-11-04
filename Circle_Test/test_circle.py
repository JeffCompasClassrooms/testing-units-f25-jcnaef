import unittest
import pytest
import math
from circle import *

class test_circle(unittest.TestCase):
    def test_init(self):
        tCircle = Circle(1)
        self.assertIsInstance(tCircle,Circle)
    
    def test_getRadius(self):
        tCircle = Circle(1)
        self.assertEqual(tCircle.getRadius(),1)
    
    def test_setRadius(self):
        tCircle = Circle(1)
        self.assertTrue(tCircle.setRadius(2))
        self.assertTrue(tCircle.setRadius(10000))

    def test_setRadiusneg(self):
        tCircle = Circle(1)
        self.assertFalse(tCircle.setRadius(-1))
    
    def test_getArea(self):
        tCircle = Circle(1)
        self.assertEqual(tCircle.getArea(),math.pi)
    
    def test_getArea2(self):
        tCircle = Circle(2)
        self.assertEqual(tCircle.getArea(),0)

    def test_getCircumference(self):
        tCircle = Circle(1)
        self.assertEqual(tCircle.getCircumference(),2*math.pi)




