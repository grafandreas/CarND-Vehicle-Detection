import glob
import cnst

    # Read in cars and notcars
def load():
    images = glob.glob('train_imgs/*/*/*.png')
    cars = [x for x in images if not "non-vehicles" in x]
    notcars = [x for x in images if  "non-vehicles" in x]
            
    return cars, notcars