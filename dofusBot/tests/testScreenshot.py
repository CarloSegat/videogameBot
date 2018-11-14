import cv2
from src.vision import getScreenShot, pilToCv2
		
def test_screenshot_and_pilToCv2():
		a = getScreenShot()
		cv2.imshow("a", pilToCv2(a))
		cv2.waitKey(0)

if __name__ ==  '__main__':
	test_screenshot_and_pilToCv2()
	
	
