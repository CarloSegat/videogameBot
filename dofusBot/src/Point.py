from math import sqrt

class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def getDistance(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y)
    
    def isAdjacent(self, point):
        '''True if point is adjacent, including on the diagonal'''
        return self.isAround(point, 2)
    
    def isAround(self, point, radius):
        return self.getDistance(point) <= radius
    
    @staticmethod
    def getCenterOfCrescent(points):
        '''Given 2d points that roughly represent a crescent return the rough center'''
        offsetToAccoutForMorePointsHavingLowerYs = 5
        sumOfX = 0
        sumOfY = 0
        for p in points:
            sumOfX = sumOfX + p.x
            sumOfY = sumOfY + p.y
        x = sumOfX / len(points)
        y = sumOfY / len(points)
        return(Point(x, y - offsetToAccoutForMorePointsHavingLowerYs))
    
    @staticmethod
    def convertToPoints(listOf2DTuples):
        points = []
        for p in listOf2DTuples:
            points.append(Point(p[0], p[1]))
        return points
    
    @staticmethod
    def swapXandY(points):
        '''Numpy indexing is Y X'''
        swapped = []
        for p in points:
            swapped.append(Point(p.y, p.x))
        return swapped
            