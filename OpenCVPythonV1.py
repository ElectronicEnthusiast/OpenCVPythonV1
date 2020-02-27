import numpy as np
import cv2 as cv
import RobotTracking #local file to track the robot


# Load a color image in grayscale
img = cv.imread('lena.jpg',0)

cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('lena.png',img)
    cv.destroyAllWindows()



robotObj = RobotTracking.RobotTracking()  # Create an empty class object

print(robotObj.Xpos)
print(robotObj.Ypos)