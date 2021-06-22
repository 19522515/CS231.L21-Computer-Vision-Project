import cv2
import numpy as np

img = cv2.imread('saitama.jpg')

width = img.shape[1]
height = img.shape[0]
channel = img.shape[2]

for r in range(360):
    image_center = tuple(np.array(img.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, r, 1.0)
    result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    cv2.imshow('a', result)
    cv2.waitKey(1)

cv2.destroyAllWindows()
