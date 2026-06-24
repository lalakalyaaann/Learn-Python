import cv2
import numpy as np 

img1= np.zeros((300,300),dtype="uint8")
img2= np.zeros((300,300),dtype="uint8")

cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2,(100,100),(250,250),255,-1)

#Bitwise operations

bit_and=cv2.bitwise_and(img1,img2)
bit_or=cv2.bitwise_or(img1,img2)
bit_not=cv2.bitwise_not(img1)

#show the result

cv2.imshow("Circle",img1)
cv2.imshow("Rectangle",img2)
cv2.imshow("AND Operation",bit_and)
cv2.imshow("OR Operation",bit_or)
cv2.imshow("Not Operation ",bit_not)

cv2.waitKey()
cv2.destroyAllWindows()