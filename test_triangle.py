# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk

I kept this^ the same as the original but:
@realauthor: Leo Papadopoulos
"""
import unittest
from Triangle import classifyTriangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
class TestTriangles(unittest.TestCase):
    """Testing for Invalid Inputs and proper functionality"""
    def test_right_triangle_a(self):
        """Testing the 3,4,5 right triangle"""
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def test_right_triangle_b(self):
        """Testing the 3,4,5 right triangle in different order to account for that error"""
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def test_equilateral_triangles(self):
        """Testing equilateral"""
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def test_zero_triangles(self):
        """Testing Invalid Input using 0,0,0"""
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput')
    def test_neg_triangles(self):
        """Testing Invalid Input for negatives"""
        self.assertEqual(classifyTriangle(-1,-2,-3), 'InvalidInput', 'No Negatives allowed')
    def test_big_triangles(self):
        """Testing inputs that exceed the range (200)"""
        self.assertEqual(classifyTriangle(201,201,201), 'InvalidInput')
    def test_isoceles_triangles(self):
        """Testing for Isoceles"""
        self.assertEqual(classifyTriangle(5,5,4), 'Isoceles')
    def test_bool_triangles(self):
        """Testing that boolean inputs give Invalid Input"""
        self.assertEqual(classifyTriangle(True, False, True), 'InvalidInput')
    def test_string_triangles(self):
        """Testing for string inputs to show Invalid Input"""
        self.assertEqual(classifyTriangle('three', 'four', 'five'), 'InvalidInput')
    def test_dec_triangles(self):
        """Testing decimal inputs. Invalid Input"""
        self.assertEqual(classifyTriangle(0.3, 0.4, 0.5), 'InvalidInput', 'No floats allowed')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()