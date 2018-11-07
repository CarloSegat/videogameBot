if __name__ ==  '__main__':
	import cv2
	import numpy as np
	from vision import getScreenShot, pilToCv2
	
	def test_subtraction_and_masking():
		image1 = cv2.imread("C:/Users/carlo/Desktop/Dofus_bot/tests/img/1a.png")
		cv2.imshow("blue", image1[:,:, RED])
		image2 = cv2.imread("C:/Users/carlo/Desktop/Dofus_bot/tests/img/1b.png")
		image3 = image1 - image2
		cv2.imshow("a",image3)
		cv2.waitKey(0)
		
	def test_masking():
		image1 = cv2.imread("C:/Users/carlo/Desktop/Dofus_bot/tests/img/1a.png")
		lower = [200, 0, 0]
		upper = [255,35, 35]
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		
		mask = cv2.inRange(image1, lower, upper)
		output = cv2.bitwise_and(image1, image1, mask = mask)
		cv2.imshow("images", np.hstack([image1, output]))
		cv2.waitKey(0)
	
	test_masking()
	test_subtraction_and_masking()
	
	
