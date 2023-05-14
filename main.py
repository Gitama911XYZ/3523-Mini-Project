import cv2
import mediapipe as mp
import serial
import numpy as np
import time
from _tkinter import *
import pyautogui

x1 , y1 , x2 , y2 = 0, 0, 0, 0
PosMin=0
PosMax=150
time.sleep(5)
ser = serial.Serial('/dev/tty.usbmodem2101',baudrate=9600,timeout=0.5)
pos = 90
def position():
      global x1, y1 ,x2, y2

webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

my_hands = mp.solutions.hands.Hands()
drawing_untils = mp.solutions.drawing_utils
while True:
      _, image = webcam.read()
      frame_height, frame_width, _ = image.shape
      rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
      output = my_hands.process(rgb_image)
      hands = output.multi_hand_landmarks
      if hands:
            for hand in hands:
                  drawing_untils.draw_landmarks(image,hand)
                  landmarks =  hand.landmark
                  for id, landmarks in enumerate (landmarks):
                        x=int(landmarks.x * frame_width)
                        y=int(landmarks.y * frame_height)
                        if id ==8:
                              cv2.circle(img=image,center=(x,y),radius=8,color=(0,255,255),thickness=3)
                              x1= x
                              y1= y
                        if id ==4:
                              cv2.circle(img=image,center=(x,y),radius=8,color=(0,0 ,255),thickness=3)
                              x2= x
                              y2 =y
                        dist = ((x2-x1)**2+(y2-y1)**2)**0.5//4
                        cv2.line(image,(x1,y1),(x2,y2),(206,159,213),5)
            #print(dist)
            pos = np.interp(dist, [10,120],[PosMin,PosMax])

            servoPos = str(pos) + '\r'
            ser.write(servoPos.encode('utf-8'))
            print('servoPos = ', servoPos)
            time.sleep(0.05)



                        
      cv2.imshow("Hand servo control using python arduino", image)
      cv2.waitKey(1)
      if cv2.waitKey(1)& 0xff==27:
         break
webcam.release()
cv2.destroyWindow()