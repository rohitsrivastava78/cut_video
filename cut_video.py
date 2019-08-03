#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:30:19 2019

@author: rohit
"""

import cv2

source_video='led1.avi';save_video=source_video.split('.')[0]+'_save.mp4'
cap = cv2.VideoCapture(source_video)
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
  
total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); 
SKIP_FRAME=1

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 5, (frame_width,frame_height))
 
video_crop_status=False
for i in range(total_frame):
    # Capture frame-by-frame
    ret, img = cap.read()
    if ret == True and i%SKIP_FRAME==0: 
        print('video frame start.........{}'.format(i))
        
        # get the key status
        k=cv2.waitKey(100)
        if k == ord('c') or video_crop_status == True:
            video_crop_status=True
            # Write the frame into the file 'output.mp4'
            out.write(img)   
            #print('video crop start.........')
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'video crop start, stop press "s" ',(10,50), font, 1,(255,255,255),2,cv2.LINE_4)
            if k == ord('s'):
                break
                 
        elif k==27:
            video_crop_status=False
            break
        else:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'press "c" button to crop video ....',(10,50), font, 1,(255,255,255),2,cv2.LINE_4)
        
        # Display the resulting frame
        cv2.imshow('video_raw',img)

# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows() 
            
