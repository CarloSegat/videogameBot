if __name__ ==  '__main__':
    import cv2
    import numpy as np
    from src.vision import scaleBy, touch, getGroupsOfCoordinates, getCenterOfCrescent
    
    realInputThreeEnemies = np.array([(303, 305), (303, 306), (303, 307), (304, 306), (304, 307), (304, 308), (304, 309), (305, 279), (305, 309), (305, 310), (306, 277), (306, 278), (306, 311), (306, 312), (307, 275), (307, 276), (307, 277), (307, 312), (307, 313), (307, 314), (308, 274), (308, 275), (308, 276), (308, 313), (308, 314), (308, 315), (309, 273), (309, 274), (309, 275), (309, 313), (309, 314), (309, 315), (309, 316), (310, 272), (310, 273), (310, 274), (310, 314), (310, 315), (310, 316), (310, 317), (311, 272), (311, 273), (311, 274), (311, 314), (311, 315), (311, 316), (311, 317), (312, 272), (312, 273), (312, 274), (312, 314), (312, 315), (312, 316), (312, 317), (313, 272), (313, 273), (313, 274), (313, 314), (313, 315), (313, 316), (313, 317), (314, 272), (314, 273), (314, 274), (314, 314), (314, 315), (314, 316), (314, 317), (315, 272), (315, 273), (315, 274), (315, 314), (315, 315), (315, 316), (315, 317), (316, 273), (316, 274), (316, 275), (316, 313), (316, 314), (316, 315), (316, 316), (317, 273), (317, 274), (317, 275), (317, 276), (317, 313), (317, 314), (317, 315), (317, 316), (318, 274), (318, 275), (318, 276), (318, 277), (318, 311), (318, 312), (318, 313), (318, 314), (318, 315), (319, 275), (319, 276), (319, 277), (319, 278), (319, 279), (319, 280), (319, 309), (319, 310), (319, 311), (319, 312), (319, 313), (319, 314), (320, 276), (320, 277), (320, 278), (320, 279), (320, 280), (320, 281), (320, 282), (320, 307), (320, 308), (320, 309), (320, 310), (320, 311), (320, 312), (320, 313), (321, 279), (321, 280), (321, 281), (321, 282), (321, 283), (321, 284), (321, 285), (321, 304), (321, 305), (321, 306), (321, 307), (321, 308), (321, 309), (321, 310), (322, 281), (322, 282), (322, 283), (322, 284), (322, 285), (322, 286), (322, 287), (322, 288), (322, 289), (322, 290), (322, 291), (322, 292), (322, 293), (322, 294), (322, 295), (322, 296), (322, 297), (322, 298), (322, 299), (322, 300), (322, 301), (322, 302), (322, 303), (322, 304), (322, 305), (322, 306), (322, 307), (322, 308), (323, 240), (323, 241), (323, 283), (323, 284), (323, 285), (323, 286), (323, 287), (323, 288), (323, 289), (323, 290), (323, 291), (323, 292), (323, 293), (323, 294), (323, 295), (323, 296), (323, 297), (323, 298), (323, 299), (323, 300), (323, 301), (323, 302), (323, 303), (323, 304), (323, 305), (323, 306), (324, 238), (324, 239), (324, 240), (324, 266), (324, 267), (324, 286), (324, 287), (324, 288), (324, 289), (324, 290), (324, 291), (324, 292), (324, 293), (324, 294), (324, 295), (324, 296), (324, 297), (324, 298), (324, 299), (324, 300), (324, 301), (324, 302), (324, 303), (325, 237), (325, 238), (325, 267), (325, 268), (326, 235), (326, 236), (326, 269), (326, 270), (327, 233), (327, 234), (327, 235), (327, 270), (327, 271), (327, 272), (328, 232), (328, 233), (328, 234), (328, 271), (328, 272), (328, 273), (329, 231), (329, 232), (329, 233), (329, 271), (329, 272), (329, 273), (329, 274), (330, 230), (330, 231), (330, 232), (330, 272), (330, 273), (330, 274), (330, 275), (331, 230), (331, 231), (331, 232), (331, 272), (331, 273), (331, 274), (331, 275), (332, 230), (332, 231), (332, 232), (332, 272), (332, 273), (332, 274), (332, 275), (333, 230), (333, 231), (333, 232), (333, 272), (333, 273), (333, 274), (333, 275), (334, 230), (334, 231), (334, 232), (334, 272), (334, 273), (334, 274), (334, 275), (335, 230), (335, 231), (335, 232), (335, 272), (335, 273), (335, 274), (335, 275), (336, 231), (336, 232), (336, 233), (336, 271), (336, 272), (336, 273), (336, 274), (337, 231), (337, 232), (337, 233), (337, 234), (337, 271), (337, 272), (337, 273), (337, 274), (338, 232), (338, 233), (338, 234), (338, 235), (338, 269), (338, 270), (338, 271), (338, 272), (338, 273), (339, 233), (339, 234), (339, 235), (339, 236), (339, 237), (339, 238), (339, 267), (339, 268), (339, 269), (339, 270), (339, 271), (339, 272), (340, 234), (340, 235), (340, 236), (340, 237), (340, 238), (340, 239), (340, 240), (340, 265), (340, 266), (340, 267), (340, 268), (340, 269), (340, 270), (340, 271), (341, 237), (341, 238), (341, 239), (341, 240), (341, 241), (341, 242), (341, 243), (341, 262), (341, 263), (341, 264), (341, 265), (341, 266), (341, 267), (341, 268), (342, 239), (342, 240), (342, 241), (342, 242), (342, 243), (342, 244), (342, 245), (342, 246), (342, 247), (342, 248), (342, 249), (342, 250), (342, 251), (342, 252), (342, 253), (342, 254), (342, 255), (342, 256), (342, 257), (342, 258), (342, 259), (342, 260), (342, 261), (342, 262), (342, 263), (342, 264), (342, 265), (342, 266), (343, 241), (343, 242), (343, 243), (343, 244), (343, 245), (343, 246), (343, 247), (343, 248), (343, 249), (343, 250), (343, 251), (343, 252), (343, 253), (343, 254), (343, 255), (343, 256), (343, 257), (343, 258), (343, 259), (343, 260), (343, 261), (343, 262), (343, 263), (343, 264), (344, 244), (344, 245), (344, 246), (344, 247), (344, 248), (344, 249), (344, 250), (344, 251), (344, 252), (344, 253), (344, 254), (344, 255), (344, 256), (344, 257), (344, 258), (344, 259), (344, 260), (344, 261), (365, 98), (365, 99), (366, 72), (366, 73), (366, 99), (366, 100), (366, 101), (367, 71), (367, 72), (367, 101), (367, 102), (368, 69), (368, 70), (368, 103), (368, 104), (369, 67), (369, 68), (369, 69), (369, 104), (369, 105), (369, 106), (370, 66), (370, 67), (370, 68), (370, 105), (370, 106), (370, 107), (371, 65), (371, 66), (371, 67), (371, 105), (371, 106), (371, 107), (371, 108), (372, 64), (372, 65), (372, 66), (372, 106), (372, 107), (372, 108), (372, 109), (373, 64), (373, 65), (373, 66), (373, 106), (373, 107), (373, 108), (373, 109), (374, 64), (374, 65), (374, 66), (374, 106), (374, 107), (374, 108), (374, 109), (375, 64), (375, 65), (375, 66), (375, 106), (375, 107), (375, 108), (375, 109), (376, 64), (376, 65), (376, 66), (376, 106), (376, 107), (376, 108), (376, 109), (377, 64), (377, 65), (377, 66), (377, 106), (377, 107), (377, 108), (377, 109), (378, 65), (378, 66), (378, 67), (378, 105), (378, 106), (378, 107), (378, 108), (379, 65), (379, 66), (379, 67), (379, 68), (379, 105), (379, 106), (379, 107), (379, 108), (380, 66), (380, 67), (380, 68), (380, 69), (380, 103), (380, 104), (380, 105), (380, 106), (380, 107), (381, 67), (381, 68), (381, 69), (381, 70), (381, 71), (381, 72), (381, 101), (381, 102), (381, 103), (381, 104), (381, 105), (381, 106), (382, 68), (382, 69), (382, 70), (382, 71), (382, 72), (382, 73), (382, 74), (382, 99), (382, 100), (382, 101), (382, 102), (382, 103), (382, 104), (382, 105), (383, 71), (383, 72), (383, 73), (383, 74), (383, 75), (383, 76), (383, 77), (383, 96), (383, 97), (383, 98), (383, 99), (383, 100), (383, 101), (383, 102), (384, 73), (384, 74), (384, 75), (384, 76), (384, 77), (384, 78), (384, 79), (384, 80), (384, 81), (384, 82), (384, 83), (384, 84), (384, 85), (384, 86), (384, 87), (384, 88), (384, 89), (384, 90), (384, 91), (384, 92), (384, 93), (384, 94), (384, 95), (384, 96), (384, 97), (384, 98), (384, 99), (384, 100), (385, 75), (385, 76), (385, 77), (385, 78), (385, 79), (385, 80), (385, 81), (385, 82), (385, 83), (385, 84), (385, 85), (385, 86), (385, 87), (385, 88), (385, 89), (385, 90), (385, 91), (385, 92), (385, 93), (385, 94), (385, 95), (385, 96), (385, 97), (385, 98), (386, 78), (386, 79), (386, 80), (386, 81), (386, 82), (386, 83), (386, 84), (386, 85), (386, 86), (386, 87), (386, 88), (386, 89), (386, 90), (386, 91), (386, 92), (386, 93), (386, 94), (386, 95)])
    realInputOneEnemy = np.array([(32, 430), (32, 431), (32, 432), (33, 431), (33, 432), (33, 433), (33, 434), (34, 404), (34, 434), (34, 435), (35, 402), (35, 403), (35, 436), (35, 437), (36, 400), (36, 401), (36, 402), (36, 437), (36, 438), (36, 439), (37, 399), (37, 400), (37, 401), (37, 438), (37, 439), (37, 440), (38, 398), (38, 399), (38, 400), (38, 438), (38, 439), (38, 440), (38, 441), (39, 397), (39, 398), (39, 399), (39, 439), (39, 440), (39, 441), (39, 442), (40, 397), (40, 398), (40, 399), (40, 439), (40, 440), (40, 441), (40, 442), (41, 397), (41, 398), (41, 399), (41, 439), (41, 440), (41, 441), (41, 442), (42, 397), (42, 398), (42, 399), (42, 439), (42, 440), (42, 441), (42, 442), (43, 397), (43, 398), (43, 399), (43, 439), (43, 440), (43, 441), (43, 442), (44, 397), (44, 398), (44, 399), (44, 439), (44, 440), (44, 441), (44, 442), (45, 398), (45, 399), (45, 400), (45, 438), (45, 439), (45, 440), (45, 441), (46, 398), (46, 399), (46, 400), (46, 401), (46, 438), (46, 439), (46, 440), (46, 441), (47, 399), (47, 400), (47, 401), (47, 402), (47, 436), (47, 437), (47, 438), (47, 439), (47, 440), (48, 400), (48, 401), (48, 402), (48, 403), (48, 404), (48, 405), (48, 434), (48, 435), (48, 436), (48, 437), (48, 438), (48, 439), (49, 401), (49, 402), (49, 403), (49, 404), (49, 405), (49, 406), (49, 407), (49, 432), (49, 433), (49, 434), (49, 435), (49, 436), (49, 437), (49, 438), (50, 404), (50, 405), (50, 406), (50, 407), (50, 408), (50, 409), (50, 410), (50, 429), (50, 430), (50, 431), (50, 432), (50, 433), (50, 434), (50, 435), (51, 406), (51, 407), (51, 408), (51, 409), (51, 410), (51, 411), (51, 412), (51, 413), (51, 414), (51, 415), (51, 416), (51, 417), (51, 418), (51, 419), (51, 420), (51, 421), (51, 422), (51, 423), (51, 424), (51, 425), (51, 426), (51, 427), (51, 428), (51, 429), (51, 430), (51, 431), (51, 432), (51, 433), (52, 408), (52, 409), (52, 410), (52, 411), (52, 412), (52, 413), (52, 414), (52, 415), (52, 416), (52, 417), (52, 418), (52, 419), (52, 420), (52, 421), (52, 422), (52, 423), (52, 424), (52, 425), (52, 426), (52, 427), (52, 428), (52, 429), (52, 430), (52, 431), (53, 411), (53, 412), (53, 413), (53, 414), (53, 415), (53, 416), (53, 417), (53, 418), (53, 419), (53, 420), (53, 421), (53, 422), (53, 423), (53, 424), (53, 425), (53, 426), (53, 427), (53, 428)])

    
    def test_get_center_of_circle():
        groups = getGroupsOfCoordinates(realInputOneEnemy, 10)
        print getCenterOfCrescent(groups[0])
    
    def test_touch():
        assert(touch((0, 0), (1,0)))
        assert(touch((4, 1), (4,2)))
        assert(touch((2, 4), (3,4)))
        assert(touch((2, 43), (2, 43)))
        assert(touch((2, 43), (3, 44)))
        assert(not touch((2, 43), (400, 43)))
    
    def test_group_coordinates():
        assert(len(getGroupsOfCoordinates(realInputThreeEnemies, 10)) == 3)       
        assert(len(getGroupsOfCoordinates(realInputOneEnemy, 10)) == 1)       
 
    def test_scaling():
        img = cv2.imread("img/1a.png")
        print img.size
        r = scaleBy(img, 0.5)
        print r.size
        r = scaleBy(r, 2)
        print r.size
        cv2.imshow("a", r)
        cv2.waitKey(0)
    
    test_get_center_of_circle()   
    test_group_coordinates()
    test_touch()
    #test_scaling()