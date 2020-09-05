import cv2

cap=cv2.VideoCapture(0)#to provide device id
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
while True:
	ret,frame=cap.read()#Read an image from specified device
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#change to gray
	if ret==False:
		continue

	faces=face_cascade.detectMultiScale(frame,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow("video frame",frame)
	
	#cv2.imshow("Video Frame",frame)#To show video frame
	#cv2.imshow("gray frame",gray_frame)

	key_pressed=cv2.waitKey(1) & 0xFF#conversion frm 32 bit to 8 bit
	if(key_pressed==ord('q')):
		break;
cap.release()#relaesing device 
cv2.destroyAllWindows()#Destroying All Windows
