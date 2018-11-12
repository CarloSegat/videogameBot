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

imgCharacterPosition = {"1b.png": [Point(130, 309)], 
                        "2b.png": [Point(837, 538)], 
                        "3b.png": [Point(753, 414)], 
                        "4a.png": [Point(543, 475)],
                        "8a.png": [Point(380, 307)] }