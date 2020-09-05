import cv2
img=cv2.imread('dog.jpg')
cv2.imshow('A dog Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()