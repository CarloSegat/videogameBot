if __name__ ==  '__main__':
	import cv2
	import numpy as np
	from src.vision import applyBlueMask,  getCoordsWhereWhite
	
	def test_subtraction_and_masking():
		image1 = cv2.imread("img/1a.png")
		image2 = cv2.imread("img/1b.png")
		image3 = image1 - image2
		cv2.imshow("a",image3)
		cv2.waitKey(0)
		
	def test_masking():
		image1 = cv2.imread("img/1a.png")
		output = applyBlueMask(image1)
		cv2.imshow("images", np.hstack([image1[:,:,0], output]))
		cv2.waitKey(0)
		
	def test_blue_finding():
		image1 = cv2.imread("img/4b.png")
		output = applyBlueMask(image1)
		coordsRowCol = getCoordsWhereWhite(output)
		print zip(coordsRowCol[0], coordsRowCol[1])
		
	test_blue_finding()
	#test_masking()
	#test_subtraction_and_masking()
	
	
