import unittest
import class_train
import class_load
import hot_windows
import cv2
import matplotlib.image as mpimg
import numpy as np

import sys


class TestStringMethods(unittest.TestCase):
    
    def test_01_ev(self):
        (svc, X_scaler) = class_train.load()
        
        image = mpimg.imread('test_images/test6.jpg')
        draw_image = np.copy(image)
        image = image.astype(np.float32)/255
        
        (hw,di) = hot_windows.hot_wins(image, draw_image, svc, X_scaler)
        print(hw)
        mpimg.imsave("unit_test/test6.jpg",di)
 

if __name__ == '__main__':
    unittest.main()