import cv2
import numpy as np
frameWidth = 640
frameHeight = 480

# Reads webcam stream 0 for the default cam subsequent no. for using other cams
cap = cv2.VideoCapture(0)

# Sets width of screen with id 3
cap.set(3, frameWidth)

# Sets height of screen with id 4
cap.set(4, frameHeight)

# Sets brightness of screen with id 10
cap.set(10, 150)

# Orange Purple Green
myColors = [[5,107,0,19,255,255], [133,5,0,159,156,255], [57,76,0,100,255,255]]

def findColor(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(color[0]), mask)

while True:
    success, img = cap.read()
    findColor(img, myColors)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
