import win32api
from keyboard import VK_CODE, press
from vision import *
from src.vision import *
#Assuming shorcuts: tactical mode = m, creature mode = m, 
# pass turn = f1

TACTICAL_MODE = 't'
CREATURE_MODE ='m'
PASS_TURN = 'F1'
SPELLS = {'longRangeAttack': '1', 'buff': '2'}
DELL_MONITOR_CROP = ((48, 21), (1254, 880))

# TODO consider how to determine when it's ur turn
# TODO move mouse out to avoid noise when taking screenshots (eg pm green trail)

def fight():
	'''Assumes the fight has just been entered'''
	ensureTacticalMode()
	ensureCreatureMode()
	ready()
	while not isFightFinished():
		startOfTurnAP = getAP()
		x, y = getScreenCoordsOfNearestEnemy()
		selectSpell(SPELLS['longRangeAttack'])
		clickScreenCoord((x, y))
		if getAP() == startOfTurnAP:
			pass
			# click w/out spells selected halfway between pg and nearest enemy
			# select an attack spell
			# click on nearest enemy
		passTurn()
	pressEsc()

def toggleTacticalMode():
	press(TACTICAL_MODE)
	
def toggleCreatureMode():
	press(CREATURE_MODE)
	
def ready():
	press('f1')
	
def ensureTacticalMode():
	'''compute # of colors in a pre/post screenshot.
	The image with lower count is more likely to be tactical mode as it's simpler'''
	pre, post = getPrePostImages(toggleTacticalMode)
	if getNumberOfColors(pre) > getNumberOfColors(post):
		toggleTacticalMode()

def	ensureCreatureMode():
	pre, post = getPrePostImages(toggleCreatureMode)
	if getNumberOfColors(pre) > getNumberOfColors(post):
		toggleCreatureMode()

def isFightFinished():
	'''Done by computing difference between screenshot 
	before and after pressing creature mode. If it's significant the fight is on
	if the images are almost identical then the fight has finished.
	Note that pressing creature mode shortcut outside a fight doesn't do anything'''
	pre, post = getPrePostImages(toggleCreatureMode)
	return areImagesSimilar(pre, post)
	
def getScreenCoordsOfNearestEnemy():
	'''Uses fact that enemies have a blue circle underneath in creature mode'''
	screen = getScreenShot()
	masked = applyBlueMask(screen)
	coordsYX = getCoordsWhereWhite(masked) 
	groupsOfCoordinates = getGroupsOfCoordinates(coordsYX, 30)
	centers = []
	for gc in groupsOfCoordinates:
		centers.append(Point.getCenterOfCrescent(gc))
	myPosition = getCharacterPosition()
	
def selectSpell(correspondingNumber):
	press(correspondingNumber)
	
def clickScreenCoord(coord):
	win32api.SetCursorPos(coord)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
	time.sleep(random.uniform(.30, .19))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

def getAP():
	pass

def getCharacterPosition():
	screen = getScreenShot()
	masked = applyRedMask(screen)
	coordsYX = getCoordsWhereWhite(masked) 
	characterCoordinates = getGroupsOfCoordinates(coordsYX, 30)
	return Point.getCenterOfCrescent(characterCoordinates)