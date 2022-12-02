import cv2
import numpy as np

cap = cv2.VideoCapture(1)
imgTarget = cv2.imread('C:/[CODE]/TargetImage.jpg')
myVid = cv2.VideoCapture('C:/[CODE]/video.mp4')

sucess, imgVideo = myVid.read()
hT,wT,cT = imgTarget.shape
imgVideo = cv2.resize(imgVideo,(wT,hT))

while True:
    sucess, imgWebcam = cap.read()
    
    

cv2.imshow('ImgTarget' , imgTarget)
cv2.imshow('myVid' , imgVideo)
cv2.imshow('Webcam', imgWebcam)
cv2.waitKey(1)


