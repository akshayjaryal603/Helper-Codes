import cv2
import math
from datetime import datetime
import os

def video_to_frame():
	for filename in os.listdir('./img/'):
	    #print(filename)
	    if filename.endswith('.jpg'):
	    	filename = './img/' + filename
	    	os.remove(filename)

	cap = cv2.VideoCapture('/home/akshay/03_labelImg_code/IC_02.mp4')
	frameRate = cap.get(5) 						#frame rate
	while(cap.isOpened()):
	    frameId = cap.get(1) 					#current frame number
	    ret, frame = cap.read()
	    if (ret != True):
	    	break
	    if (frameId % math.floor(frameRate) == 0):
	    	filename = "./img/frame2_" +  str(int(frameId)) + ".jpg"
	    	cv2.imwrite(filename, frame)

	    key = cv2.waitKey(1)
	    								# press 'q' to exit the window
	    if key == ord('q'):
	    	if status == 1:
	    		time.append(datetime.now())
	    	break

	cap.release()
	cv2.destroyAllWindows()
	print ("Done!")

# function calling
video_to_frame()

'''
import cv2

cap = cv2.VideoCapture('output.avi')
framerate = cap.get(cv2.cv.CV_CAP_PROP_FPS)
framecount = 0

while(True):
    # Capture frame-by-frame
    success, image = cap.read()
    framecount += 1

    # Check if this is the frame closest to 10 seconds
    if framecount == (framerate * 2)
      framecount = 0
      cv2.imshow('image',image)

    # Check end of video
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''
