'''
This file contains helper functions that are shared 
across multiple modules.

Keeping common utilities here avoids 
code duplication
and makes the code easier to maintain
'''
import cv2
import numpy as np
import time

def resize_frame(frame,width=640,height=360):

    ''' 
    Resize the camera frame to a fixed resolution

    Why:
    1)Improves performance
    2)Keeps processing stable across devices
    '''
    return cv2.resize(frame,(width,height))

def estimate_brightness(frame):
    '''Estimate ambient brightness of the frame.
    Method :
        1.Convert to grayscale
        2.Take mean pixel intensity
    Used for :
    1)Automatic day/night mode switching
    '''
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    return float(np.mean(gray))

def calculate_fps(prev_time):
    '''Calculate frames-per second(FPS).
    Why:
    1)Confirms real-time performance.
    2)Help detect performance regressions

    '''

    current_time = time.time()
    fps = 1.0/max(current_time-prev_time,1e-6)
    return fps,current_time

def draw_label(frame,text,position=(10,30)):
    '''Draw readable text overlay on the videoframe
     Used for:
     1)Displaying mode
     2)Motion intensity
     3)FPS

    '''
    cv2.putText(
               frame,
               text,
               position,
               cv2.FONT_HERSHEY_SIMPLEX,
               0.9,
               (255,255,255),
               2,
               cv2.LINE_AA
               )

def is_motion_spike(motion_pixels,threshold=1500):
    '''
    Detect unusually large motion
    events.

    This is useful for :
    1)Saves frame automatically
    2)Triggering alerts
    3)Future ML labeling
    '''

    return motion_pixels >threshold