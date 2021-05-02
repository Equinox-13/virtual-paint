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

# Orange Blue Green
myColors = [[0,103,0,161,255,255], [83,90,58,179,249,255], [10,83,187,179,249,255]]

def findColor(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        getContours(mask)
        # cv2.imshow(str(color[0]), mask)

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print("area===========>",area)    
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
            perimeter = cv2.arcLength(cnt, True)
            print("perimeter---------->", perimeter)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors)
    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
