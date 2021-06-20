import cv2
import numpy as np

def First(animation, img, height, weight):
    for i in range(0,height,5):
        animation[height+100-i:,50:weight+50] = img[:i,:]
        cv2.imshow("Animation", animation)
        cv2.waitKey(100)
def Second(animation, img, height, weight):
    for i in range(0,100,5):
        animation[:,:]=0
        animation[100-i:100+height-i, 50:weight+50] = img[:,:]
        cv2.imshow("Animation", animation)
        cv2.waitKey(100) 
def Third(animation, img, height, weight):
    for i in range(0,height,5):
        animation[:,:]=0
        animation[:height-i,50:weight+50] = img[i:,:]
        cv2.imshow("Animation", animation)
        cv2.waitKey(100)
def CreateImg():
    img = np.zeros((600,1000,3), np.uint8)
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(img,'Thank you for watching!',(35,120), font, 2.7,(0,0,255),3,cv2.LINE_4)
    font_normal = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(img,'Nguyen Loc Linh - 19521754',(350,220), font_normal, 0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.putText(img,'Le Duong Khanh Viet - 19522515',(325,280), font_normal, 0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.putText(img,'Tran Duy Quang - 19522102',(350,340), font_normal, 0.5,(255,255,255),1,cv2.LINE_AA)
    meme = cv2.imread('Meme.jpg') #recommend file Meme.jpg on github
    img[450:450+meme.shape[0],370:370+meme.shape[1]]=meme[:,:]
    return img, 600, 800


img, height, weight = CreateImg()
height = img.shape[0]
weight = img.shape[1]
animation = np.zeros((height+100, weight+100,3), np.uint8)

First(animation, img, height, weight)
Second(animation, img, height, weight)
Third(animation, img, height, weight)
cv2.destroyAllWindows()

