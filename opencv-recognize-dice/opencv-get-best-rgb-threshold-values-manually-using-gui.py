# orignal source https://stackoverflow.com/a/26044115

import cv2
import numpy as np


image = cv2.imread('pics_3_/image 3(2).jpg')
image = image[:, 154:601]
image = cv2.resize(image, (0,0), fx=1.0, fy=1.0)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def nothing(x):
    pass

# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
lower_r, lower_g, lower_b = 100,100,100
upper_r, upper_g, upper_b = 100,100,100


# Creating lower track bar
cv2.createTrackbar('lower_r', 'result', 0, 255, nothing)
cv2.createTrackbar('lower_g', 'result', 0, 255, nothing)
cv2.createTrackbar('lower_b', 'result', 0, 255, nothing)

# Creating upper track bar
cv2.createTrackbar('upper_r', 'result', 0, 255, nothing)
cv2.createTrackbar('upper_g', 'result', 0, 255, nothing)
cv2.createTrackbar('upper_b', 'result', 0, 255, nothing)

while(1):
    # get info from track bar and appy to result
    lower_r = cv2.getTrackbarPos('lower_r', 'result')
    lower_g = cv2.getTrackbarPos('lower_g', 'result')
    lower_b = cv2.getTrackbarPos('lower_b', 'result')

    upper_r = cv2.getTrackbarPos('upper_r', 'result')
    upper_g = cv2.getTrackbarPos('upper_g', 'result')
    upper_b = cv2.getTrackbarPos('upper_b', 'result')

    # Normal masking algorithm
    lower = np.array([lower_r, lower_g, lower_b])   # normally 0,0,0
    upper = np.array([upper_r, upper_g, upper_b])

    mask = cv2.inRange(rgb, lower, upper)

    # result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('result',mask)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# cap.release()

cv2.destroyAllWindows()
