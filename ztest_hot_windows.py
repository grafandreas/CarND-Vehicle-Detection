import unittest
import class_train
import class_load
import hot_windows
import cv2
import matplotlib.image as mpimg
import numpy as np
import cnst

import sys

sizes = [32,48,64,80,96,112,128,144,160]

class TestStringMethods(unittest.TestCase):
    
    def test_01_ev(self):
        (svc, X_scaler) = class_train.load()
        
        image =cnst.img_read_f('test_images/test6.jpg')
        for s in sizes:
            draw_image = np.copy(image)
            
            (hw,di) = hot_windows.hot_wins(image, draw_image, svc, X_scaler,xy_window=(s,s))
            print(hw)
            mpimg.imsave("unit_test/test6_"+str(s)+".jpg",di)
 
    def test_01_multi(self):
        (svc, X_scaler) = class_train.load()
        
        image =cnst.img_read_f('test_images/test6.jpg')
        
        draw_image = np.copy(image)
        
        (hw,di) = hot_windows.multi_hot_wins(image, draw_image, svc, X_scaler,cnst.sizes)
        print(hw)
        mpimg.imsave("unit_test/test6_multi.jpg",di)

if __name__ == '__main__':
    unittest.main()