import cv2
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade= cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade= cv2.CascadeClassifier("haarcascade_smile.xml")

cap= cv2.VideoCapture(0)

while True :
    ret,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face= face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in face :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    #detects the face and searches for everything inside it 
    roi_gray=gray[y:y+h,x:x+w]
    roi_color= frame[y:y+h,x:x+w]

    eyes=eye_cascade.detectMultiScale(roi_gray,1.1,10)
    if len(eyes)>0:
        cv2.putText(frame,"Eyes Detected!",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)

    smile=eye_cascade.detectMultiScale(roi_gray,1.7,10)
    if len(smile)>0:
        cv2.putText(frame,"Smile Detected!",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
    
    cv2.imshow("Smart Face Detector",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()