import cv2
import numpy as np
import math

def Solve(height, weight):
    a = -3*math.sqrt(2*height)/weight
    b = -math.sqrt(2*height)
    c = 1/2*height
    temp = [[a,b,c]]
    a = -4*math.sqrt(2*height)/weight
    b = -5*math.sqrt(2*height)/12
    c = 7/8*height
    temp.append([a,b,c])
    a = -12*math.sqrt(height)/weight
    b = -math.sqrt(height)/4
    c = 15/16*height
    temp.append([a,b,c])
    return temp
def Animation(temp,X4,X2,X0,animation,img):
    a, b, c = temp[0][0], temp[0][1], temp[0][2]
    for i in range(int(X4), int(X2),10):
        x = i
        y = int((a*x+b)**2+c)
        #print(x,y)
        animation[:,:]=0
        animation[:y,:weight+x] = img[height-y:,-x:]
        cv2.imshow("Animation",animation)
        cv2.waitKey(50)
    
    a, b, c = temp[1][0], temp[1][1], temp[1][2]
    for i in range(int(X2), int(X0),10):
        x = i
        y = int((a*x+b)**2+c)
        #print(x,y)
        animation[:,:]=0
        animation[:y,:weight+x] = img[height-y:,-x:]
        cv2.imshow("Animation",animation)
        cv2.waitKey(50)
    
    a, b, c = temp[2][0], temp[2][1], temp[2][2]
    for i in range(int(X0), 0,1):
        x = i
        y = int((a*x+b)**2+c)
        #print(x,y)
        animation[:,:]=0
        animation[:y,:weight+x] = img[height-y:,-x:]
        cv2.imshow("Animation",animation)
        cv2.waitKey(1)

img = cv2.imread('Captain.jpg')
height, weight = img.shape[0], img.shape[1]
animation = np.zeros((height, weight,3), np.uint8)
X2 = -1/3*weight
X1 = -1/6*weight
X0 = -1/24*weight
arr = Solve(height,weight)
Animation(arr, X2, X1, X0, animation, img)

cv2.destroyAllWindows()
