from lesson_functions import bin_spatial, color_hist, get_hog_features, draw_boxes, slide_window

from features import bin_spatial, search_windows
import cnst

import hotspots

hs = hotspots.Hotspots(history_size=5,heat=5)

def hot_wins(image,draw_image, svc, X_scaler, xy_window=(96, 96), xy_overlap=(0.5, 0.5),):

    
    windows = slide_window(image, x_start_stop=[None, None], y_start_stop=cnst.y_start_stop, 
                        xy_window=xy_window, xy_overlap=xy_overlap)
    
    hot_windows = search_windows(image, windows, svc, X_scaler, color_space=cnst.color_space, 
                            spatial_size=cnst.spatial_size, hist_bins=cnst.hist_bins, 
                            orient=cnst.orient, pix_per_cell=cnst.pix_per_cell, 
                            cell_per_block=cnst.cell_per_block, 
                            hog_channel=cnst.hog_channel, spatial_feat=cnst.spatial_feat, 
                            hist_feat=cnst.hist_feat, hog_feat=cnst.hog_feat)                       
    
    #window_img = draw_boxes(draw_image, hot_windows, color=(0, 0, 255), thick=6)     
    window_img = draw_image
    return hot_windows, window_img


def multi_hot_wins(image,draw_image, svc, X_scaler, sizes, xy_overlap=(0.5, 0.5)):
    hot_windows=[]
    for s in sizes:
        (hw,di) = hot_wins(image, draw_image, svc, X_scaler,(s,s),xy_overlap)
        hot_windows.append(hw)
        
#     print(hot_windows)
    w2=[]
    for e in hot_windows:
        if(len(e)>0):
            e = e[0]
    #         print(e)
    #         print(e[0][0])
    #         print(e[1][1])
            w2.append([e[0][0],e[0][1],e[1][0],e[1][1]])
#     print("--")
#     print(w2)
    hs.push(w2)
    hs.calcHotspots()
#     print(hs.getHistory())
#     print(hs.getLayers())
#     hs.drawHotspots(1280, 720,di)
    hs.drawFound(1280, 720,di)
    return hot_windows,di
        