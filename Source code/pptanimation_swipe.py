import cv2
import numpy as np

img = cv2.imread('images/saitama.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert it to hsv


width = img.shape[1]
height = img.shape[0]
channel = img.shape[2]

increase_v = 40
decrease_s = 10
step = 2

# bien doi hinh anh
print("chon huong di cua animation: ")
print("1.Left -> Right")
print("2.Right -> Left")
print("3.Down")
print("4.Up")
flag = input()

if flag == '3':
    # huong di xuong
    for y in range(1, height, step):
        h, s, v = cv2.split(hsv[0: y, :])

        v = np.where(v <= 255 - increase_v, v + increase_v, 255)
        s = np.where(s >= 0 + decrease_s, s - decrease_s, 0)

        hsv[0: y, :] = cv2.merge((h, s, v))

        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('animation', img)
        cv2.waitKey(1)
elif flag == '1':
    # huong sang phai
    for x in range(1, width, step):
        h, s, v = cv2.split(hsv[:, 0: x])

        v = np.where(v <= 255 - increase_v, v + increase_v, 255)
        s = np.where(s >= 0 + decrease_s, s - decrease_s, 0)

        hsv[:, 0:x] = cv2.merge((h, s, v))

        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('animation', img)
        cv2.waitKey(1)
elif flag == '2':
    # huong sang trai
    for x in range(width - 2, 0, -step):
        h, s, v = cv2.split(hsv[:, x: -1])

        v = np.where(v <= 255 - increase_v, v + increase_v, 255)
        s = np.where(s >= 0 + decrease_s, s - decrease_s, 0)

        hsv[:, x:-1] = cv2.merge((h, s, v))

        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('animation', img)
        cv2.waitKey(1)
elif flag == '4':
    # huong len tren
    for y in range(height - 2, 0, -step):
        h, s, v = cv2.split(hsv[y: -1, :])

        v = np.where(v <= 255 - increase_v, v + increase_v, 255)
        s = np.where(s >= 0 + decrease_s, s - decrease_s, 0)

        hsv[y: -1, :] = cv2.merge((h, s, v))

        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('animation', img)
        cv2.waitKey(1)
else:
    print('nhap cac gia tri tu 1 den 4')
cv2.destroyAllWindows()
