import cv2
import numpy as np
import math
img = cv2.imread('saitama.png')

width = img.shape[1]
height = img.shape[0]
channel = img.shape[2]

margin = 0
radius = int(math.sqrt((width // 2) ** 2 + (height // 2) ** 2))
center = (center_x, center_y) = (width//2, height//2)
thickness = int(radius / 50)
white = (255, 255, 255)
red = (0, 0, 255)

for angle in range(360):
    tip_x = center_x + radius * math.cos(angle * np.pi / 180.0)
    tip_y = center_y + radius * math.sin(angle * np.pi / 180.0)
    cv2.line(img, center, (int(tip_x), int(tip_y)), white, thickness)
    cv2.imshow('img', img)
    cv2.waitKey(1)
cv2.destroyAllWindows()
