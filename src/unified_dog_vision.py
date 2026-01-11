'''
Main entry point of the project.

This file:
1.Captures camera frames
2.Automatically switches day/night modes
3.logs metrics
4.Displays output in real real time
'''

import cv2
import numpy as np
import time

from vision_day import dog_day_vision
from vision_night import dog_night_vision
from metrics import init_logger,log_metrics
from utils import(resize_frame,estimate_brightness,calculate_fps,draw_label)
    
#Brightness threshold for mode

DAY_THRESHOLD =30
NIGHT_THRESHOLD =60

#Intialize camera

cap =cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,360)

prev_gray =None
current_mode ='DAY'

#Init logger
init_logger()
prev_time = time.time()

while True :
    ret,frame =cap.read()
    if not ret:
        break
    brightness =estimate_brightness(frame)


    #Preprocessing 
    frame = resize_frame(frame)
    brightness = estimate_brightness(frame)

    #Decide which mode to use
    if brightness >DAY_THRESHOLD:
     current_mode == 'DAY'

    elif brightness <NIGHT_THRESHOLD:
     current_mode == 'NIGHT_THRESHOLD'
     current_mode == 'NIGHT'

    #Run approriate vision pipeline
    if current_mode == 'DAY':
        output,prev_gray,motion_pixels =dog_day_vision(frame,prev_gray)
    else:
        output,prev_gray,motion_pixels =dog_day_vision(frame,prev_gray)

    #Calculate performance 
    fps,prev_time =calculate_fps(prev_time
                             )
    #Log metrics
    log_metrics(brightness,motion_pixels,current_mode,fps)

    #Display info
    draw_label(output,f'{current_mode}|Motion:{motion_pixels}|FPS:{fps:.1f}')

    cv2.imshow('Bio-Inspired Low light Motion Perception',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    ##clean up
cap.release()
cv2.destroyAllWindows()