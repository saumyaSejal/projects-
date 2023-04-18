from keras.models import load_model 
from time import sleep
#import tensorflow as tf 
#from tf.keras.utils import img_to_array  
#from keras.preprocessing.image import img_to_array
from keras.preprocessing import image 
#from keras.preprocessing.image import img_to_array
import cv2
import numpy as np 

face_classifier=cv2.CascadeClassifier(r'C:\Users\saumy\OneDrive - vit.ac.in\Desktop\AIproj\haarcascade_frontalface_default.xml')#harcascade file path(raw file path) 
classifier_labels=load_model(r'C:\Users\saumy\OneDrive - vit.ac.in\Desktop\AIproj\model.h5')#model.h5 file path

emotion_labels=['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']

cap=cv2.VideoCapture(0) #vedio capture default capture from laptop camera 

while True:
    _,frame=cap.read()
    labels=[]
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detetctionMultiScale(gray)

    for(x,y,w,h) in faces:                                     #for each face we will form an rectangle and right the emotion 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA) #because my moel needs 48x48 image



        if(np.sum([roi_gray])!=0):
            roi=roi_gray.astype('float')/255.0
            roi=img_to_array(roi)
            roi=np.expand_dims(roi,axis=0)

            prediction=classifier_labels.predict(roi)[0]
            label=emotion_labels[prediction.argmax()]
            label_position=(x,y-10)

            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,255),2)

        else:
            cv2.putText(frame,"NO FACES",(30,80),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("Emotion Detector",frame)
    if(cv2.waitKey(1) &0xFF == ord('q')):
        break

    cap.release()
    cv2.destroyAllWindows()
