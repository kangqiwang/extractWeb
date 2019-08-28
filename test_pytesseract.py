import numpy as np
import cv2 as cv
img = cv.imread('screenshot1.png')
# edge=cv.Canny(img,5,10)

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
'''
screen_res = 1280, 720
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

#cv.namedWindow('dst_rt', cv.WINDOW_NORMAL)
#cv.resizeWindow('dst_rt', window_width, window_height)
'''


cv.namedWindow('image', cv.WINDOW_NORMAL)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0,255,0), 3)
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()





#imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
#ret, thresh = cv.threshold(imgray, 127, 255, 0)
#im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#cv.drawContours(img, contours, -1, (0,255,0), 3)
