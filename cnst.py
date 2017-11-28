import matplotlib.image as mpimg
import cv2

y_start_stop = [400, 656] # Min and max in y to search in slide_window()
color_space = 'RGB' # Can be RGB, HSV, LUV, HLS, YUV, YCrCb
orient = 9  # HOG orientations
pix_per_cell = 8 # HOG pixels per cell
cell_per_block = 2 # HOG cells per block
hog_channel = 'ALL' #0 # Can be 0, 1, 2, or "ALL"
spatial_size = (16, 16) # Spatial binning dimensions
hist_bins = 16    # Number of histogram bins
spatial_feat = True # Spatial features on or off
hist_feat = True # Histogram features on or off
hog_feat = True # HOG features on or off
sizes = [160,144,128,112,96]
#sizes = [96,112,128,144,160]
#sizes = [32,48,64,80,96,112,128,144,160]
img_dimensions=(1280,720)
    
def img_read_f(x):
    return ldc(x)
    
def ldm(f):
    return mpimg.imread(f)

def ldc(f):
    img = cv2.imread(f)
    return  cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
