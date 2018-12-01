import numpy as np
import cv2
import os
from pathlib import Path


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


videotxt = open('videoNums.txt')
number = videotxt.readlines() #this is the variable that we add 1 to if a video file already exists
videotxt.close()
int_lst = [int(x) for x in number] # converts number to int list
str1 = ''.join(str(e) for e in int_lst) # converts int_lst to string
vidNum = str1 + "1" 
savevidNo = int(vidNum) #we cant save the video with the variable vidNum as its a str so we use this variable and save it as an ints
VIDEONUMBER = int(savevidNo)
NAMEFILE = str(VIDEONUMBER)
VideoName = (NAMEFILE + ".avi")
exists = str(str1)

my_file = Path(exists + ".avi")
if my_file.is_file():
    
    replace_line('videoNums.txt',0,vidNum)
    print(vidNum)



cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(VideoName,fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()





