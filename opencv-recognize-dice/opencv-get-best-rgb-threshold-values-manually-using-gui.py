# orignal source https://stackoverflow.com/a/26044115

import cv2
import numpy as np


image = cv2.imread('dices (2).jpg')
image = cv2.resize(image, (0,0), fx=0.3, fy=0.3)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def nothing(x):
    pass

# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
lower_h, lower_s, lower_v = 100,100,100
upper_h, upper_s, upper_v = 100,100,100


# Creating lower track bar
cv2.createTrackbar('lower_h', 'result', 0, 179, nothing)
cv2.createTrackbar('lower_s', 'result', 0, 255, nothing)
cv2.createTrackbar('lower_v', 'result', 0, 255, nothing)

# Creating upper track bar
cv2.createTrackbar('upper_h', 'result', 0, 179, nothing)
cv2.createTrackbar('upper_s', 'result', 0, 255, nothing)
cv2.createTrackbar('upper_v', 'result', 0, 255, nothing)

while(1):
    # get info from track bar and appy to result
    lower_h = cv2.getTrackbarPos('lower_h', 'result')
    lower_s = cv2.getTrackbarPos('lower_s', 'result')
    lower_v = cv2.getTrackbarPos('lower_v', 'result')

    upper_h = cv2.getTrackbarPos('upper_h', 'result')
    upper_s = cv2.getTrackbarPos('upper_s', 'result')
    upper_v = cv2.getTrackbarPos('upper_v', 'result')

    # Normal masking algorithm
    lower = np.array([lower_h, lower_s, lower_v])   
    upper = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, lower, upper)

    # result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('result',mask)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# cap.release()

cv2.destroyAllWindows()
