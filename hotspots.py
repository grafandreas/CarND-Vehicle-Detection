'''
Created on 25.11.2017

@author: andreas
'''

import rectangles
import numpy as np
import cv2
from collections import deque

class Hotspots:
    '''
    classdocs
    '''
    
    def push(self,rl):
        self.history.append(rl)
    
    def getHistory(self):
        return self.history
    
    def initLayers(self):
        self.layers = []
        for i in range(self.heat):
            self.layers.append([])
            
    def calcHotspots(self):
        self.initLayers()
        currentLayer = 0;
        for historyElement in self.history:
            self.addToLayer(currentLayer,historyElement)
        return self.layers[self.heat-1]
            
    def addToLayer(self,layer,l):
        if(layer >= self.heat):
            return None
        
        isect = self.rs.intersectList(self.layers[layer],l)
        for x in l:
            if x not in self.layers[layer]:
                self.layers[layer].append(x)
                
        self.addToLayer(layer+1,isect)
        return isect
        
    def getLayers(self):
        return self.layers
    
    def drawHotspots(self,width,height,blank_image=None):
        if blank_image is None:
            blank_image = np.zeros((height,width,3), np.uint8)
            
        clevl = int(255 / self.heat)
        print(clevl)
        for i,l in enumerate(self.layers):
            for r in l:
                color= (clevl*(i+1),clevl*(i+1),0)
                print(color)
                print(r)
                cv2.rectangle(blank_image,(r[0],r[1]),(r[2],r[3]),
                              color,1)
        return blank_image
    
    def drawFound(self,width,height,blank_image=None):
        if blank_image is None:
            blank_image = np.zeros((height,width,3), np.uint8)
        
        cl = self.rs.cluster(self.layers[self.heat-1])
        for r in cl:
            cv2.rectangle(blank_image,(r[0],r[1]),(r[2],r[3]),
                              (255,0,0),5)
    
    def __init__(self,history_size=10,heat=3):
        '''
        Constructor
        '''
        self.rs = rectangles.Rectangles()
        self.history = deque(maxlen=history_size)
        self.heat = heat
        
        
        
    
        