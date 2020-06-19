# pip install Pillow if you don't already have it

# import image utilities
from PIL import Image
from imutils import paths
# import os utilities
import os
import cv2

# define a function that rotates images in the current directory
# given the rotation in degrees as a parameter
def rotateImages(rotationAmt):
	# for each image in the current directory    # os.getcwd()
  	imagePaths = list(paths.list_images(os.getcwd()))
  	for image in imagePaths:
	  	#print(image)
	    # open the image
	    #img = Image.open(image)
	    img = cv2.imread(image)
	    # rotate and save the image with the same filename
	    img.rotate(rotationAmt).save(image)
	    # close the image
	    img.close()
    
# examples of use
rotateImages(90)
#rotateImages(180)
#rotateImages(270)
