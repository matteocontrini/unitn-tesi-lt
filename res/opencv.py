#!/usr/bin/python3
import cv2 # pip install opencv-python==4.1.0.25

vid = cv2.VideoCapture("rtsp.mp4")

while vid.isOpened():
    ret, img = vid.read()

    if not ret:
        break

    average = img.mean(axis=0).mean(axis=0)

    b, g, r = average
    diff = g - ((r + b) / 2)

    millis = vid.get(cv2.CAP_PROP_POS_MSEC) / 1000
    print(str(millis) + " => " + str(diff))
