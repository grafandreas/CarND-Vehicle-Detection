import unittest
import class_load
import sys
import class_train
import sklearn.svm.classes
import sklearn.preprocessing.data

class TestStringMethods(unittest.TestCase):
    
    def test_01_train(self):
        print(sys.version)
        svc= class_train.train()
        
    def test_02_load(self):
        r = class_train.load()
        self.assertEqual(2, len(r))
        print(type(r[0]))
        print(type(r[1]))
        self.assertIs(type(r[0]), sklearn.svm.classes.LinearSVC )
        self.assertIs(type(r[1]), sklearn.preprocessing.data.StandardScaler)

 

if __name__ == '__main__':
    unittest.main()