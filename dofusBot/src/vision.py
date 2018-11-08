import pyscreenshot as ImageGrab
import cv2
import PIL
import numpy as np
from imageop import scale

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

def applyBlueMask(img):
	'''Returns 1 channel immage where white represent a blue pixel in original'''
	lower = np.array([200, 0, 0], dtype = "uint8")
	upper = np.array([255,35, 35], dtype = "uint8")
	mask = cv2.inRange(img, lower, upper)
	return mask

def getCoordsWhereWhite(img):
	if(len(img.shape)> 2):
		raise Exception("method takes a 1 channel img")
	return np.where(img > 200)

def getGroupsOfCoordinates(arrayOf2DCoords, threshold):
	'''Input: 2d points
	Output: lists of "bucket-fill-neighbours" whose number is above threshold'''
	clusters = []
	while arrayOf2DCoords.any():
		cluster = [arrayOf2DCoords[0]]
		arrayOf2DCoords = arrayOf2DCoords[1:]
		i = 0
		while i < len(arrayOf2DCoords):
			try:
				for point in cluster:
					if(touch(point, arrayOf2DCoords[i])):
						cluster.append(arrayOf2DCoords[i])	
						arrayOf2DCoords = arrayOf2DCoords[np.arange(len(arrayOf2DCoords))!=i]
						i = 0
						break
				i = i + 1
			except IndexError:
				break
		if len(cluster) > threshold:
			clusters.append(cluster)		
	return clusters

def touch(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) <= 2

def getCenterOfCrescent(points):
	'''Given 2d points that roughly represent a crescent return the rough center'''
	offsetToAccoutForMorePointsHavingLowerYs = 5
	sumOfX = 0
	sumOfY = 0
	for p in points:
		sumOfX = sumOfX + p[0]
		sumOfY = sumOfY + p[1]
	x = sumOfX / len(points)
	y = sumOfY / len(points)
	return(x, y + offsetToAccoutForMorePointsHavingLowerYs)
		
		
def scaleBy(img, scaleFactor):
	width = int(img.shape[1] * scaleFactor)
	height = int(img.shape[0] * scaleFactor)
	return cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
	
		
		