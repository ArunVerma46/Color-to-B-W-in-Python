import cv2

# For Load the image
image = cv2.imread('C:/Users/Welcome/Desktop/New folder (2)/car.jpg')
if image is None:
    print("Error Loading Image")
    exit()

# Convert to grayscale (black and white)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Display the grayscale image
cv2.imshow('Black and White Image', gray)
cv2.waitKey(0)              # We use this for Pause and wait until the user presses a key, if don't use this window open and immediately close.
cv2.destroyAllWindows()     # We use this for close all the image windows that were opened. after the user presses a key, it will clean up and close everything.

#Optionally, save the grayscale image
cv2.imwrite('black and white.jpg', gray)
