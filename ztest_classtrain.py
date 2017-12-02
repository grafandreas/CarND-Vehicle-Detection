import unittest
import class_load
import sys
import class_train
import sklearn.svm.classes
import sklearn.preprocessing.data
import itertools

class TestStringMethods(unittest.TestCase):
    
    def test_01_train(self):
        print(sys.version)
        svc= class_train.train()
        
    def xtest_02_load(self):
        r = class_train.load()
        self.assertEqual(2, len(r))
        print(type(r[0]))
        print(type(r[1]))
        self.assertIs(type(r[0]), sklearn.svm.classes.LinearSVC )
        self.assertIs(type(r[1]), sklearn.preprocessing.data.StandardScaler)

    def xtest_01_parameter_eval(self):
        print(sys.version)
        (c,nc) = class_load.load()
#         B=[['RGB','YCrCb','YUV','HLS','LUV','HSV'],[9],[0,1,2,'ALL'],[8],[2]]
        B=[['YUV'],[13],['ALL'],[8],[2]]
        combis = list(itertools.product(*B))
        print(combis)
        accs = []
        
        for cs in combis:
            print(cs)
            (svc,a)= class_train.train_p(c,nc,cs[0],cs[1],cs[2],cs[3],cs[4])
            accs.append(a)
         
        for i in range(len(combis)):
            print(str(combis[i]) +" : "+str(accs[i]))   
        

if __name__ == '__main__':
    unittest.main()