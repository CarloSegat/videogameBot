from src.vision import applyBlueMask, getCoordsWhereWhite
if __name__ ==  '__main__':
    import cv2
    import numpy as np
    from src.vision import scaleBy, getGroupsOfCoordinates
    from src.Point import Point
    BaseImgPath = "img/"
    imgNumberOfEnemies = {"1b.png": 3, "2b.png": 2, "3b.png": 1,
                          "5a.png": 1, "8a.png": 1, "9a.png": 8, "10a.png": 5}
    imgCentersOfEnemies = {"1b.png": [Point(88, 372), Point(256, 329), Point(295, 310)], 
                           "2b.png": [Point(1086, 331), Point(1214, 267)], 
                           "3b.png": [Point(670, 582)], 
                           "5a.png": [Point(1129, 229)] }
    creatureMode_OffOn = {"1a.png": "1b.png", "2a.png": "2b.png", "3a.png": "3b.png"}
    tacticalMode_OffOn = {"6a.png": "6b.png", "7a.png": "7b.png", "8a.png": "8b.png"}
    fight_InOut = {"5a": "5b", "8b": "8c"}
    
    def test_get_center_of_circle():
        realInputOneEnemy = Point.convertToPoints(np.array([(32, 430), (32, 431), (32, 432), (33, 431), (33, 432), (33, 433), (33, 434), (34, 404), (34, 434), (34, 435), (35, 402), (35, 403), (35, 436), (35, 437), (36, 400), (36, 401), (36, 402), (36, 437), (36, 438), (36, 439), (37, 399), (37, 400), (37, 401), (37, 438), (37, 439), (37, 440), (38, 398), (38, 399), (38, 400), (38, 438), (38, 439), (38, 440), (38, 441), (39, 397), (39, 398), (39, 399), (39, 439), (39, 440), (39, 441), (39, 442), (40, 397), (40, 398), (40, 399), (40, 439), (40, 440), (40, 441), (40, 442), (41, 397), (41, 398), (41, 399), (41, 439), (41, 440), (41, 441), (41, 442), (42, 397), (42, 398), (42, 399), (42, 439), (42, 440), (42, 441), (42, 442), (43, 397), (43, 398), (43, 399), (43, 439), (43, 440), (43, 441), (43, 442), (44, 397), (44, 398), (44, 399), (44, 439), (44, 440), (44, 441), (44, 442), (45, 398), (45, 399), (45, 400), (45, 438), (45, 439), (45, 440), (45, 441), (46, 398), (46, 399), (46, 400), (46, 401), (46, 438), (46, 439), (46, 440), (46, 441), (47, 399), (47, 400), (47, 401), (47, 402), (47, 436), (47, 437), (47, 438), (47, 439), (47, 440), (48, 400), (48, 401), (48, 402), (48, 403), (48, 404), (48, 405), (48, 434), (48, 435), (48, 436), (48, 437), (48, 438), (48, 439), (49, 401), (49, 402), (49, 403), (49, 404), (49, 405), (49, 406), (49, 407), (49, 432), (49, 433), (49, 434), (49, 435), (49, 436), (49, 437), (49, 438), (50, 404), (50, 405), (50, 406), (50, 407), (50, 408), (50, 409), (50, 410), (50, 429), (50, 430), (50, 431), (50, 432), (50, 433), (50, 434), (50, 435), (51, 406), (51, 407), (51, 408), (51, 409), (51, 410), (51, 411), (51, 412), (51, 413), (51, 414), (51, 415), (51, 416), (51, 417), (51, 418), (51, 419), (51, 420), (51, 421), (51, 422), (51, 423), (51, 424), (51, 425), (51, 426), (51, 427), (51, 428), (51, 429), (51, 430), (51, 431), (51, 432), (51, 433), (52, 408), (52, 409), (52, 410), (52, 411), (52, 412), (52, 413), (52, 414), (52, 415), (52, 416), (52, 417), (52, 418), (52, 419), (52, 420), (52, 421), (52, 422), (52, 423), (52, 424), (52, 425), (52, 426), (52, 427), (52, 428), (52, 429), (52, 430), (52, 431), (53, 411), (53, 412), (53, 413), (53, 414), (53, 415), (53, 416), (53, 417), (53, 418), (53, 419), (53, 420), (53, 421), (53, 422), (53, 423), (53, 424), (53, 425), (53, 426), (53, 427), (53, 428)]))
        pointWhereToClickEnemy = Point.getCenterOfCrescent(Point.swapXandY(realInputOneEnemy))
        expectedCenter = Point(419,41)
        assert(pointWhereToClickEnemy.isAround(expectedCenter, 5))
        
    def test_from_img_to_numberOfEnemies():
        for img in imgNumberOfEnemies:
            try:
                image = cv2.imread(BaseImgPath + img)
                assert(not image is None)
                masked = applyBlueMask(image)
                assert(len(masked)> 50)
                coordsYX = getCoordsWhereWhite(masked)
                assert(len(coordsYX) > 100)
                groupsOfCoordinates = getGroupsOfCoordinates(coordsYX, 30)
                assert(len(groupsOfCoordinates) == imgNumberOfEnemies[img])
            except Exception as e:
                print type(e)
                print img + " didn't work. Expected: " + str(imgNumberOfEnemies[img]) + " but got " + str(len(groupsOfCoordinates))
                exit()
                
    def test_from_img_to_centersOfEnemies():
        for img in imgCentersOfEnemies:
            try:
                image = cv2.imread(BaseImgPath + img)
                masked = applyBlueMask(image)
                coordsYX = getCoordsWhereWhite(masked)  
                groupsOfCoordinates = getGroupsOfCoordinates(coordsYX, 20)
                for group in groupsOfCoordinates:
                    computedCenter = Point.getCenterOfCrescent(group)
                    expectedCenters = imgCentersOfEnemies[img]
                    #assert(len(computedCenter) == len(expectedCenters))
                    oneMatch = False
                    for exp in expectedCenters:
                        oneMatch = oneMatch or computedCenter.isAround(exp, 10)
                    assert(oneMatch) 
            except Exception as e:
                print type(e)
                print img + " didn't work"   
                exit()         
                
    def test_scaling():
        img = cv2.imread("img/1a.png")
        print img.size
        r = scaleBy(img, 0.5)
        print r.size
        r = scaleBy(r, 2)
        print r.size
        cv2.imshow("a", r)
        cv2.waitKey(0)
        
    test_from_img_to_numberOfEnemies()
    test_from_img_to_centersOfEnemies()
    test_get_center_of_circle()   
    print "All good :)"