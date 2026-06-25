import cv2
image = cv2.imread("pentagon.png")
gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh =cv2.threshold(gray_image,240,255,cv2.THRESH_BINARY)

#find contours 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#draw contours
cv2.drawContours(image, contours,-1,(0,255,0),3)

for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    corner=len(approx)

    if corner==3:
        shape_name="Triangle"
    elif corner==4:
        shape_name="Rectangle"
    elif corner==5:
        shape_name="Pentagon"
    elif corner==6:
        shape_name="Circle"
    else:
        shape_name="Unknown"

    cv2.drawContours(image,[approx],0,(0,255,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[0]-10
    cv2.putText(image,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,0,0))

cv2.imshow("Contours image",image)
cv2.waitKey()
cv2.destroyAllWindows()