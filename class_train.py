import class_load
from skimage.feature import hog
import glob
from sklearn.preprocessing import StandardScaler
from sklearn.svm import  LinearSVC
import lesson_functions 
from lesson_functions import extract_features, bin_spatial, color_hist, get_hog_features, draw_boxes, slide_window
from sklearn.model_selection import  train_test_split
import time
import numpy as np
import cv2
import pickle
import cnst

def train():
    (cars,notcars) = class_load.load()
    

    
    
    car_features = extract_features(cars, color_space=cnst.color_space, 
                            spatial_size=cnst.spatial_size, hist_bins=cnst.hist_bins, 
                            orient=cnst.orient, pix_per_cell=cnst.pix_per_cell, 
                            cell_per_block=cnst.cell_per_block, 
                            hog_channel=cnst.hog_channel, spatial_feat=cnst.spatial_feat, 
                            hist_feat=cnst.hist_feat, hog_feat=cnst.hog_feat)
    notcar_features = extract_features(notcars, color_space=cnst.color_space, 
                            spatial_size=cnst.spatial_size, hist_bins=cnst.hist_bins, 
                            orient=cnst.orient, pix_per_cell=cnst.pix_per_cell, 
                            cell_per_block=cnst.cell_per_block, 
                            hog_channel=cnst.hog_channel, spatial_feat=cnst.spatial_feat, 
                            hist_feat=cnst.hist_feat, hog_feat=cnst.hog_feat)
    
    X = np.vstack((car_features, notcar_features)).astype(np.float64)                        
    # Fit a per-column scaler
    X_scaler = StandardScaler().fit(X)
    # Apply the scaler to X
    scaled_X = X_scaler.transform(X)
    
    # Define the labels vector
    y = np.hstack((np.ones(len(car_features)), np.zeros(len(notcar_features))))
    
    
    # Split up data into randomized training and test sets
    rand_state = np.random.randint(0, 100)
    X_train, X_test, y_train, y_test = train_test_split(
        scaled_X, y, test_size=0.2, random_state=rand_state)
    
    print('Using:',cnst.orient,'orientations',cnst.pix_per_cell,
        'pixels per cell and', cnst.cell_per_block,'cells per block')
    print(len(X_train))
    print('Feature vector length:', len(X_train[0]))
    print('Feature vector length:', len(X_train[1]))
    # Use a linear SVC 
    svc = LinearSVC()
    # Check the training time for the SVC
    t=time.time()
    svc.fit(X_train, y_train)
    t2 = time.time()
    print(round(t2-t, 2), 'Seconds to train SVC...')
    # Check the score of the SVC
    print('Test Accuracy of SVC = ', round(svc.score(X_test, y_test), 4))
    # Check the prediction time for a single sample
    t=time.time()
    pickle.dump(svc, open( "svc.p", "wb" ))
    pickle.dump(X_scaler, open( "scaler.p", "wb" ))
    return svc

def load():
    return pickle.load( open( "svc.p", "rb" ) ), pickle.load(open( "scaler.p", "rb" ))