'''
Created on 25.11.2017

@author: andreas
'''
import unittest
import hotspots
import cv2

TEST_OUT="unit_test"


class TestHotspots(unittest.TestCase):


    def test_historyLen(self):
        hp = hotspots.Hotspots(3)
        for i in range(0,5):
            hp.push([i])
            
        self.assertEquals(3,len(hp.getHistory()))
        self.assertEquals([2],hp.getHistory()[0])
        
    def test_OnlyOne(self):
        hp = hotspots.Hotspots(5)
        hp.push([[0,1,9,10]])
        r = hp.calcHotspots()
        print(r)
        ls = hp.getLayers()
        print(ls)
        
    def test_Simple(self):
        hp = hotspots.Hotspots(5)
        hp.push([[0,1,9,10]])
        hp.push([[0,1,9,10]])
        hp.push([[0,1,9,10]])
        r = hp.calcHotspots()
        print(r)
        ls = hp.getLayers()
        print(ls)
        
    def test_Together(self):
        hp = hotspots.Hotspots(5)
        hp.push([[0,1,9,10]])
        hp.push([[1,2,9,10]])
        hp.push([[2,3,9,10]])
        r = hp.calcHotspots()
        print(r)
        ls = hp.getLayers()
        print(ls)
        img = hp.drawHotspots(1280, 720)
        img =  cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        cv2.imwrite(TEST_OUT+"/hotspots.jpg",img)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()