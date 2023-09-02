import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')




webcam = cv2.VideoCapture(0)
# key = cv2.waitKey(1)
while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x,y,w,h) in face_cordinates:
        cv2.rectangle(frame, (x,y),  (x+w, y+h), (0,256,0),2 )
                                #(0,256,0) randrange(128,256)
    cv2.imshow('saikiran detector ', frame)
    key =cv2.waitKey(1)
    if key==81 or key==113:
        break

webcam.release()   
print("code completed")
"""
face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)

for (x,y,w,h) in face_cordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(128,256),randrange(128,256), randrange(128,256)),2 ) 
# [[299 307  66  66]]
# print(face_cordinates)


cv2.imshow('saikiran detector ', img)
cv2.waitKey()
print("code completed")
"""
