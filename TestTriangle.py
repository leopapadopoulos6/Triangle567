# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
<<<<<<< HEAD
       
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testZeroTriangles(self):
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput')

    def testNegTriangles(self):
        self.assertEqual(classifyTriangle(-1,-2,-3), 'InvalidInput', 'No Negatives allowed')

    def testBigTriangles(self):
        self.assertEqual(classifyTriangle(201,201,201), 'InvalidInput')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(5,5,4), 'Isoceles')

    def testBoolTriangles(self):
        self.assertEqual(classifyTriangle(True, False, True), 'InvalidInput')

    def testStringTriangles(self):
        self.assertEqual(classifyTriangle('three', 'four', 'five'), 'InvalidInput')
    
    def testDecTriangles(self):
        self.assertEqual(classifyTriangle(0.3, 0.4, 0.5), 'InvalidInput', 'No floats allowed')
=======
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
>>>>>>> 0817963b30b3b93510d28c4dd77ca9390729cb20

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

