import cv2
import numpy as np

image = cv2.imread("gorilla.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

circles = cv2.HoughCircles(blurred,cv2.HOUGH_GRADIENT,dp=1.2,minDist=30,param1=50,param2=30,minRadius=10,maxRadius=100)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

cv2.imshow("Detected Circles", image)
print(len(circles) if circles is not None else 0)
cv2.waitKey(0)
cv2.destroyAllWindows()