from testData import *
import os, cv2
from src.vision import applyRedMask, getCoordsWhereWhite, getGroupsOfCoordinates, crop

def test_character_position():
    for img in imgCharacterPosition:
        try:
            image = cv2.imread(BaseImgPath + img)
            assert(not image is None)
            masked = applyRedMask(image)
            assert(len(masked) > 80)
            masked = crop(masked, (48, 21), (1254, 880))
            cv2.imshow("d", masked)
            cv2.waitKey(0)
            coordsYX = getCoordsWhereWhite(masked) 
            characterCoordinates = getGroupsOfCoordinates(coordsYX, 30)
            print len(characterCoordinates)
            # 2 centers because ocra is red
            # actually just one using transparency
            center = Point.getCenterOfCrescent(characterCoordinates[0])
            #center2 = Point.getCenterOfCrescent(characterCoordinates[1])
            print str(center.addOffset((48, 21))) +" " + img
        except Exception as e:
            print os.path.basename(__file__) + " :( :( :("
            raise Exception(str(os.path.basename(__file__)) + " failed :( :( :(") 
        
if __name__ == "__main__":
    test_character_position()