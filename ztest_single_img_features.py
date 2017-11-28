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
import class_load


class TestStringMethods(unittest.TestCase):
    
    def test_01_trainingset(self):
        images = glob.glob('train_imgs/vehicles/GTI_Far/image0000.png')
        (clf,scaler) = class_train.load()
        for i in images:
            img = cnst.img_read_f(i)
            test_img = cv2.resize(img, (64, 64))  
            features = single_img_features(test_img,color_space=cnst.color_space, 
                            spatial_size=cnst.spatial_size, hist_bins=cnst.hist_bins, 
                            orient=cnst.orient, pix_per_cell=cnst.pix_per_cell, 
                            cell_per_block=cnst.cell_per_block, 
                            hog_channel=cnst.hog_channel, spatial_feat=cnst.spatial_feat, 
                            hist_feat=cnst.hist_feat, hog_feat=cnst.hog_feat)
            print(features.shape)
            print(features)
            print(len(features))
            test_features = scaler.transform(np.array(features).reshape(1, -1))
            #test_features = features
            prediction = clf.predict(test_features)
            print(str(prediction)+" : "+i)

    def test_02_trainingset(self):
        images = glob.glob('train_imgs/vehicles/*/*.png')
        (clf,scaler) = class_train.load()
        counter = 0
        for i in images:
            img = cnst.img_read_f(i)
            test_img = cv2.resize(img, (64, 64))  
            features = single_img_features(test_img,color_space=cnst.color_space, 
                            spatial_size=cnst.spatial_size, hist_bins=cnst.hist_bins, 
                            orient=cnst.orient, pix_per_cell=cnst.pix_per_cell, 
                            cell_per_block=cnst.cell_per_block, 
                            hog_channel=cnst.hog_channel, spatial_feat=cnst.spatial_feat, 
                            hist_feat=cnst.hist_feat, hog_feat=cnst.hog_feat)
 
            test_features = scaler.transform(np.array(features).reshape(1, -1))
            #test_features = features
            prediction = clf.predict(test_features)
            if(prediction < 1.0):
                print("Prediction "+str(prediction)+" for "+i)
                counter = counter+1
                
        print((len(images)-counter)/len(images))
                
    def test_02_trainingse_nont(self):
        images = glob.glob('train_imgs/non-vehicles/*/*.png')
        (clf,scaler) = class_train.load()
        counter = 0
        for i in images:
            img = cnst.img_read_f(i)
            test_img = cv2.resize(img, (64, 64))  
            features = single_img_features(test_img,color_space=cnst.color_space, 
                            spatial_size=cnst.spatial_size, hist_bins=cnst.hist_bins, 
                            orient=cnst.orient, pix_per_cell=cnst.pix_per_cell, 
                            cell_per_block=cnst.cell_per_block, 
                            hog_channel=cnst.hog_channel, spatial_feat=cnst.spatial_feat, 
                            hist_feat=cnst.hist_feat, hog_feat=cnst.hog_feat)
 
            test_features = scaler.transform(np.array(features).reshape(1, -1))
            #test_features = features
            prediction = clf.predict(test_features)
            if(prediction >0.0):
                print("Prediction "+str(prediction)+" for "+i)
                counter = counter+1
                
        print((len(images)-counter)/len(images))

if __name__ == '__main__':
    unittest.main()