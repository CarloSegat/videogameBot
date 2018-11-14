from src.vision import getNumberOfColors, crop
from testData import tacticalMode_Off_On, BaseImgPath, creatureMode_OffOn
import cv2

def test_test_tactical_mode():
    for off in tacticalMode_Off_On:
        pre = cv2.imread(BaseImgPath + off)
        post = cv2.imread(BaseImgPath +  tacticalMode_Off_On[off])
        assert(len(pre) > 0)
        assert(getNumberOfColors(pre) > getNumberOfColors(post))
        
def test_creature_mode():
    for off in creatureMode_OffOn:
        pre = crop(cv2.imread(BaseImgPath + off), (48, 21), (1254, 880))
        post = crop(cv2.imread(BaseImgPath + creatureMode_OffOn[off]), (48, 21), (1254, 880))
        assert(len(pre) > 0)
        assert(getNumberOfColors(pre) > getNumberOfColors(post))
        
if __name__ == "__main__":
    test_test_tactical_mode()
    test_creature_mode()