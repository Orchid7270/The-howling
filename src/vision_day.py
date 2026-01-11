'''
Implements daytime dogvision simulation
Dogs:
 See blue and yellow well
 see red and green poorly
 Are sensitive to motion
'''
import cv2
import numpy as np

# Hsv ranges for colors dogs can see well
Lower_Yellow =np.array([20,100,100])
Upper_Yellow =np.array([40,255,255])
Lower_Blue =np.array([100,50,50]) 
Upper_Blue =np.array([130,255,255])  

def dog_day_vision(frame,prev_gray):
    
    '''Simulate dog vision during daytime.
    Steps:
     1.Keep blue and yellow colors
     2.Convert other colors to gray
     3.Enhance motion perception
    '''

    hsv =cv2.cvtColor (frame,cv2.COLOR_BGR2HSV)

    yellow_mask =cv2.inRange(hsv,Lower_Yellow,Upper_Yellow)
    blue_mask =cv2.inRange(hsv,Lower_Blue,Upper_Blue)
    color_mask =cv2.bitwise_or(yellow_mask,blue_mask)
   
   #Keep visible colors
    color_view = cv2.bitwise_and(frame,frame,mask=color_mask)
    #Conver rest to grayscale
    gray_bg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_bg =cv2.cvtColor(gray_bg,cv2.COLOR_GRAY2BGR)

    inv_mask = cv2.bitwise_not(color_mask)
    bg_view =cv2.bitwise_and(gray_bg,gray_bg,mask=inv_mask)
    output = cv2.add(color_view,bg_view)
   
   #Motion detection using frame differencing
   
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(11,11),0)
    
    if prev_gray is not None:
        motion = cv2.absdiff(prev_gray,gray)
        _,motion =cv2.threshold(motion,25,255,cv2.THRESH_BINARY)
        motion_pixels = int((motion > 0).sum())

        #Overlay motion

        motion = cv2.cvtColor(motion,cv2.COLOR_GRAY2BGR)
        output = cv2.addWeighted(output,1.0,motion,0.25,0)

    else:
        motion_pixels = 0

    return output,gray,motion_pixels