from src.Point import Point
import numpy as np

def test_Point():
    a = Point(0, 0)
    b = Point(2, 3)
    c = Point(1, 0)
    d = Point
    arrayTuples = [(2,2), (88,2), (0, 2)]
 
    assert(a.isAdjacent(c))
    assert( not a.isAdjacent(b))
    assert(a.getDistance(c) == 1)
    assert(a.getDistance(a) == 0)
    assert(a.isAround(b, 5))
    assert(not a.isAround(b, 4))
    
    points = Point.convertToPoints(arrayTuples)
    for i in range(len(points)):
        assert(points[i].x == arrayTuples[i][0]) 
        
    print __file__.split("\\")[-1] + " passed"  
    
if __name__ ==  '__main__':
    test_Point()