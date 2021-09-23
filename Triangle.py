# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk

I kept this^ the same as the original but:
@realauthor: Leo Papadopoulos
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type

    #I moved this to the top to sort out the type before checking if its b/w 0-200
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
      
    # require that the input values be >= 0 and <= 200
    
    #b <= 0 ----> b<= 0
    #put them in same if statement instead of separate because made tests fail
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    elif a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle

    #had to correct mathematical bug
    if (a <= (b - c)) or (b <= (a - c)) or (c <= (b - a)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    #changed the right triangle formaula becuase other one was assuming C is always going to be hypotenuse.
    #hypotenuse can be any of the sides so formula should reflect
    elif (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'
