
'''
Created on 25.11.2017

@author: andreas
'''

import numpy as np


class Rectangles:
    '''
    classdocs
    '''

    def intersect(self, r1, r2):
        res = [np.max([r1[0],r2[0]]), 
               np.max([r1[1],r2[1]]),
               np.min([r1[2],r2[2]]),
               np.min([r1[3],r2[3]])]
        
        if( res[2] <= res[0] or  res[3] <= res[1]):
            return None
        else:
            return res
        
    def intersectList(self,l1,l2):
        res=[]
        for i1 in l1:
            for i2 in l2:
                x = self.intersect(i1, i2)
                if(x != None):
                    res.append(x)
        return res
    
        
    def __init__(self):
        '''
        Constructor
        '''
        