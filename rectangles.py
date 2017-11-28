
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
    
    def cluster(self,l):
        to_process = list(l)
        res=[]
        loopFlag=True
        while len(to_process)>0 :
            p = to_process[0]
            to_process
            rmv=[p]
#             print(".")
#             print(p)
            for i in range(1,len(to_process)):
                o = to_process[i]
#                 print(o)
#                 print(self.intersect(p, o))
                if self.intersect(p, o) is not None:
                    p=[np.min([p[0],o[0]]),
                       np.min([p[1],o[1]]),
                       np.max([p[2],o[2]]),
                       np.max([p[3],o[3]])
                       ]
                    rmv.append(o)
            res.append(p)
            to_process = [x for x in to_process if x not in rmv]
        return res
    
        
    def __init__(self):
        '''
        Constructor
        '''
        