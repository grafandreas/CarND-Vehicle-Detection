import unittest
import class_train
import class_load
import hot_windows
import cv2
import matplotlib.image as mpimg
import numpy as np
import features
import glob
from features import single_img_features
import sys
import cnst



class TestStringMethods(unittest.TestCase):
    
    def test_01_eval(self):
        images = glob.glob('train_imgs/vehicles/*/*.png')
        (clf,scaler) = class_train.load()
        for i in images:
            img = mpimg.imread(i)
            test_img = cv2.resize(img, (64, 64))  
            features = single_img_features(test_img,color_space=cnst.color_space, 
                            spatial_size=cnst.spatial_size, hist_bins=cnst.hist_bins, 
                            orient=cnst.orient, pix_per_cell=cnst.pix_per_cell, 
                            cell_per_block=cnst.cell_per_block, 
                            hog_channel=cnst.hog_channel, spatial_feat=cnst.spatial_feat, 
                            hist_feat=cnst.hist_feat, hog_feat=cnst.hog_feat)
            print(features.shape)
            test_features = scaler.transform(np.array(features).reshape(1, -1))
            #test_features = features
            prediction = clf.predict(test_features)
            print(str(prediction)+" : "+i)
 

if __name__ == '__main__':
    unittest.main()