import pyscreenshot as ImageGrab
import cv2
import PIL
import numpy as np

def getScreenShot(box = (0,0, 1279, 1023)):
	return ImageGrab.grab(box)
	
def pilToCv2(pilImg):
	'''opencv2 uses GBR, PIL uses RGB'''
	return cv2.cvtColor(np.array(pilImg), cv2.COLOR_RGB2BGR)
	
def getPrePostImages(toggleAction):
	preScreenShot = getScreenShot()
	toggleAction()
	postScreenShot = getScreenShot()
	toggleAction()
	return (preScreenShot, postScreenShot)
	
def getNumberOfColors(img):
	'''Img --> # of different colors'''
	return len(getColors(img))
	
def getColors(img):
	'''Img -> list of colors'''
	img = img.convert('RGB')
	colors_present = []
	for x in range(0, img.size[0]):
		for y in range(0, img.size[1]):
			colors_present.append(img.getpixel((x,y)))
	return list(set(colors_present))
	
def areImagesSimilar(imgLHS, imgRHS):
	'''Simple pixel checking. If images are identical te subtraction will give a completly 
	black image.'''
	subtraction = imgLHS - imgRHS
	return isPercentageBlack(subraction, 50)
	
def isPercentageBlack(img, percentage):
	# check if it's PIL or opencv img
	return cv2.countNonZero(img) >= percentage
		