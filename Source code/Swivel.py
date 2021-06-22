import cv2
import numpy as np

def MinimizeSize(img0,size,originalImage):
    begin=0
    for j in range(1,size,30):
        begin = int((img0.shape[1]-(size-j))/2)
        img0[:,:begin]=0
        img0[:,begin:begin+size-j] = cv2.resize(originalImage, (size-j, originalImage.shape[0]), interpolation = cv2.INTER_AREA)
        img0[:,begin+size-j:]=0
        cv2.imshow('animation', img0)
        cv2.waitKey(1)
def MaximizeSize(img0,size,flipHorizontal):
    for j in range(1,size,30):
        begin = int((img0.shape[1]-j)/2)
        img0[:,:begin]=0
        img0[:,begin:begin+j] = cv2.resize(flipHorizontal, (j, flipHorizontal.shape[0]), interpolation = cv2.INTER_AREA)
        img0[:,begin+j:]=0
        cv2.imshow('animation', img0)
        cv2.waitKey(1)


originalImage = cv2.imread('Captain.jpg')
flipHorizontal = cv2.flip(originalImage, 1)
img0 = np.zeros((originalImage.shape[0],originalImage.shape[1]+100,3), np.uint8)
size = originalImage.shape[1]
for i in range(3):
    if (i%2==0):
        MinimizeSize(img0, size, originalImage)
        MaximizeSize(img0, size, flipHorizontal)
    else:
        MinimizeSize(img0, size, flipHorizontal)
        MaximizeSize(img0, size, originalImage)
cv2.destroyAllWindows()

