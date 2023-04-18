#haarcascade is a pretrained model that will be used to detect face 

import cv2 as cv 

capture =cv.VideoCapture(0) #0 as parameter to access laptop cam 

pretrainedModel=cv.CascadeClassifier(r"C:\Users\saumy\OneDrive - vit.ac.in\Desktop\AIproj\haarcascade_frontalface_default.xml")

#we use while loop to capture frames continously 

while True:
    bool,frame=capture.read()
    if(bool == True):
        grayScale=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        coordList=pretrainedModel.detectMultiScale(grayScale,scaleFactor=1.1,minNeighbors=3)
        #coordinate list is a list of tuples with x and y coordinates of rectangle around the face 


        #drawing rectangle 
        for(x,y,w,h) in coordList:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv.imshow("Face Detection Test",frame)

        if(cv.waitKey(20) == ord('x')):
            break

capture.release()
cv.destroyAllWindows()