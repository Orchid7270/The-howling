'''Implements night-time dog vision simulation

At night dogs:
1.Rely almost entirely on rods.
2.Focus on motion and contrast
3.Donot rely on color

'''
import cv2
import numpy as np

def dog_night_vision(frame,prev_grey):
    
    '''Simulate dog vision

    Steps:

    1.Convert to grayscale
    2.Amplify brightness
    3.Enhance edges
    4.Detect motion
    '''
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Light amplification (tapetum lucidum approximation)
     
    amplified = cv2.convertScaleAbs(gray,alpha =3.0,beta =25)
    amplified = cv2.GaussianBlur(amplified,(5,5),0)

    #Edge detection helps shape perception

    edges = cv2.Canny(amplified,40,120)
    edges = cv2.dilate(edges,None)

    #Motion detection

    if prev_grey is not None:
        _,motion =cv2.threshold(motion,25,255,cv2.THRESH_BINARY)
        motion = cv2.medianBlur(motion,5)
        motion_pixels =int((motion > 0).sum())
    else:
        motion =np.zeros_like(amplified)
        motion_pixels = 0
    
    #Combine layers
    output =cv2.addWeighted(amplified,0,8,edges,0.6,0)
    output =cv2.addWeighted(output,1.0,motion,0.4,0)

    #Convert back to 3-channel for display
    output =cv2.cvtColor(output,cv2.COLOR_GRAY2BGR)

    return output,amplified,motion_pixels
