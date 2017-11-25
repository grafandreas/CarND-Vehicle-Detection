'''
Created on 25.11.2017

@author: andreas
'''
import unittest
import rectangles

class RectanglesTest(unittest.TestCase):


    def testIdent(self):
        rs = rectangles.Rectangles()
        r = rs.intersect([0,1,9,10], [0,1,9,10])
        self.assertEqual([0,1,9,10],r)
        

    def test_Disjunct(self):
        rs = rectangles.Rectangles()
        r = rs.intersect([0,1,9,10], [30,31,39,30])
        self.assertEqual(None,r)
        
    def test_Intersect(self):
        rs = rectangles.Rectangles()
        r = rs.intersect([0,1,9,10], [5,6,14,15])
        self.assertEqual([5,6,9,10],r)
        
    def test_IntersectList(self):
        rs = rectangles.Rectangles()
        r = rs.intersectList([[0,1,9,10], [5,6,14,15]],[[30,31,39,30]])
        self.assertEqual(0, len(r))
        
    def test_IntersectList2(self):
        rs = rectangles.Rectangles()
        r = rs.intersectList([[0,1,9,10], [5,6,14,15]],[[6,7,7,8]])
        self.assertEqual(2, len(r))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()