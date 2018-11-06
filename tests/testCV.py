if __name__ ==  '__main__':
	import cv2, numpy
	from vision import getScreenShot, pilToCv2
	a = getScreenShot()
	cv2.imshow("a", pilToCv2(a))
	cv2.waitKey(0)
