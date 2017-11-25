import unittest
import videoprocess as uut
import numpy as np
import cv2
import class_train
import class_load
import hot_windows
import cv2
import matplotlib.image as mpimg
import numpy as np

import sys

IMG_DIR="project_video.mp4"
TEST_OUT="unit_test"

(svc, X_scaler) = class_train.load()
 
class TestVideo(unittest.TestCase):
    
 

   

    def test_pipe(self):
       
        uut.process(IMG_DIR,TEST_OUT+"/L"+IMG_DIR,cb_ok)#,subC=(5,7))

  
        
        
    

def cb(img) :
    return img    

def cb_ok(image):
    draw_image = np.copy(image)
    image = image.astype(np.float32)/255
        
    (hw,di) = hot_windows.hot_wins(image, draw_image, svc, X_scaler)
    return di

    
if __name__ == '__main__':
    unittest.main()