import pyscreenshot as ImageGrab
import cv2
import PIL
import numpy as np
from imageop import scale
from Point import Point

def getScreenShot(box = (0,0, 1279, 1023)):
	'''Gets cursor out of the wat for a clean shot'''
	Point(0,0).hover()
	return ImageGrab.grab(box)
	
def pilToCv2(pilImg):
	'''opencv2 uses GBR, PIL uses RGB'''
	return cv2.cvtColor(np.array(pilImg), cv2.COLOR_RGB2BGR)
	
def getPrePostImages(toggleAction):
	'''Return 2 sshots representing screen before and after an action'''
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
	return np.unique(img.reshape(-1, img.shape[2]), axis=0)
	
def areImagesSimilar(imgLHS, imgRHS):
	'''Simple pixel checking. If images are identical te subtraction will give a completly 
	black image.'''
	subtraction = imgLHS - imgRHS
	return isPercentageBlack(subtraction, 50)
	
def isPercentageBlack(img, percentage):
	'''Does the image have more than percentage-specified black pixels?'''
	count = 0
	img = img.reshape(-1, img.shape[2])
	for pix in img:
		if pix[0] == pix[1] == pix[2] == 0:
			count = count + 1
	return count / float(img.shape[0]) >= percentage * 0.01

def applyMask(img, lower, upper):
	mask = cv2.inRange(img, lower, upper)
	return mask

def applyBlueMask(img):
	'''Returns 1 channel immage where white represent a blue pixel in original
	The bonds are defined considering the shades of blues present when using
	transparent mode'''
	lower = np.array([180, 0, 0], dtype = "uint8")
	upper = np.array([255, 80, 80], dtype = "uint8")
	return applyMask(img, lower, upper)
	
def applyRedMask(img):
	'''Returns 1 channel immage where white represent a blue pixel in original
	The bonds are defined considering the shades of blues present when using
	transparent mode'''
	lower = np.array([0, 0, 180], dtype = "uint8")
	upper = np.array([80, 80, 255], dtype = "uint8")
	return applyMask(img, lower, upper)

def getCoordsWhereWhite(img):
	if(len(img.shape)> 2):
		raise Exception("method takes a 1 channel img")
	columnRow = np.where(img > 200)
	coordsXY = zip(columnRow[1], columnRow[0])
	return Point.convertToPoints(coordsXY)

def getGroupsOfCoordinates(points, threshold):
	'''Input: 2d points
	Output: lists of "bucket-fill-neighbours" whose number is above threshold'''
	if not isinstance(points[0], Point):
		raise Exception("Pass array of points")
	clusters = []
	while points.any():
		cluster = [points[0]]
		points = points[1:]
		i = 0
		while i < len(points):
			try:
				for point in cluster:
					if point.isAround(points[i], 3):
						cluster.append(points[i])	
						points = points[np.arange(len(points))!=i]
						i = 0
						break
				i = i + 1
			except IndexError:
				break
		if len(cluster) > threshold:
			clusters.append(cluster)	
	return clusters	
		
def scaleBy(img, scaleFactor):
	width = int(img.shape[1] * scaleFactor)
	height = int(img.shape[0] * scaleFactor)
	return cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
	
def crop(img, leftUp, rightDown):
	return img[leftUp[1]:rightDown[1], leftUp[0]:rightDown[0]]
		