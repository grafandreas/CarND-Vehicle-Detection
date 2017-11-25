from lesson_functions import extract_features, bin_spatial, color_hist, get_hog_features, draw_boxes, slide_window
from features import bin_spatial, search_windows
import cnst
def hot_wins(image,draw_image, svc, X_scaler):

    
    windows = slide_window(image, x_start_stop=[None, None], y_start_stop=cnst.y_start_stop, 
                        xy_window=(96, 96), xy_overlap=(0.5, 0.5))
    
    hot_windows = search_windows(image, windows, svc, X_scaler, color_space=cnst.color_space, 
                            spatial_size=cnst.spatial_size, hist_bins=cnst.hist_bins, 
                            orient=cnst.orient, pix_per_cell=cnst.pix_per_cell, 
                            cell_per_block=cnst.cell_per_block, 
                            hog_channel=cnst.hog_channel, spatial_feat=cnst.spatial_feat, 
                            hist_feat=cnst.hist_feat, hog_feat=cnst.hog_feat)                       
    
    window_img = draw_boxes(draw_image, hot_windows, color=(0, 0, 255), thick=6)     
    
    return hot_windows, window_img