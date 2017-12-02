'''
Created on 25.11.2017

@author: andreas
'''

import rectangles
import numpy as np
import cv2
from collections import deque
from scipy.ndimage.measurements import label


class Hotspots:
    '''
    classdocs
    '''
    
    def push(self,rl):
        self.history.append([(x[0],x[1],x[2],x[3]) for x in rl ])
    
    def getHistory(self):
        return self.history
    
    def initLayers(self):
        self.layers = []
        for i in range(self.heat):
            self.layers.append(set([]))
            
    def calcHotspotsX(self):
        self.initLayers()
        currentLayer = 0;
        for historyElement in self.history:
            self.addToLayer(currentLayer,historyElement)
        return self.layers[self.heat-1]
    
    def calcHotspots(self):
        heatmap = np.zeros((720,1280))
        for historyElement in self.history:
            lh = np.zeros((720,1280))
            print(historyElement)
            for box in historyElement:
                print(box)
                lh[box[1]:box[3], box[0]:box[2]] = 1
                heatmap = np.add(heatmap,lh)
                
        heatmap[heatmap <= self.heat] = 0      
        self.heatmap = heatmap
        labels = label(heatmap)
        return self.heatmapsToBoxes(labels)
          
    def heatmapsToBoxes(self,labels):
        boxes = []
        for car_number in range(1, labels[1]+1):
            # Find pixels with each car_number label value
            nonzero = (labels[0] == car_number).nonzero()
            # Identify x and y values of those pixels
            nonzeroy = np.array(nonzero[0])
            nonzerox = np.array(nonzero[1])
            # Define a bounding box based on min/max x and y
            bbox = ((np.min(nonzerox), np.min(nonzeroy)), (np.max(nonzerox), np.max(nonzeroy)))
            boxes.append(bbox)
        self.boxes = boxes
        return boxes
            
    def addToLayer(self,layer,l):
        if(layer >= self.heat):
            return None
        
        isect = self.rs.intersectList(self.layers[layer],l)
        for x in l:
#             print("_--")
#             print(x)
#             print(self.layers)
#             print(self.layers[layer])
            if x not in self.layers[layer]:
                self.layers[layer].add(x)
                
        self.addToLayer(layer+1,isect)
        return isect
        
    def getLayers(self):
        return self.layers
    
    def drawHotspots(self,width,height,blank_image=None):
        if blank_image is None:
            blank_image = np.zeros((height,width,3), np.uint8)
            
        clevl = int(255 / self.heat)
#         print(clevl)
        for i,l in enumerate(self.layers):
            for r in l:
                color= (clevl*(i+1),clevl*(i+1),0)
#                 print(color)
#                 print(r)
                cv2.rectangle(blank_image,(r[0],r[1]),(r[2],r[3]),
                              color,1)
        return blank_image
    
    def drawFoundX(self,width,height,blank_image=None):
        if blank_image is None:
            blank_image = np.zeros((height,width,3), np.uint8)
        
        cl = self.rs.cluster(self.layers[self.heat-1])
        for r in cl:
            cv2.rectangle(blank_image,(r[0],r[1]),(r[2],r[3]),
                              (255,0,0),5)
            
    def drawFound(self,width,height,blank_image=None):
#         print(blank_image.shape)
#         print(self.heatmap.shape)
#         cv2.addWeighted(blank_image, 1, self.heatmap, 0.3, 0)
        for r in self.boxes:
#             print(r)
            cv2.rectangle(blank_image,(r[0][0],r[0][1]),(r[1][0],r[1][1]),
                              (255,0,0),5)
    
    def __init__(self,history_size=10,heat=3):
        '''
        Constructor
        '''
        self.rs = rectangles.Rectangles()
        self.history = deque(maxlen=history_size)
        self.heat = heat
        
        
        
    
        