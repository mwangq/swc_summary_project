def closest_point(x0,y0,x1,y1,datapoints):
    assert len(datapoints) > 0, 'There should be datapoints'
    
    (m,b) = line_equation(x0,y0,x1,y1)
    
    min_dist = distance_from_point(m,b,datapoints[0][0],datapoints[0][1])
    for point in datapoints:
        this_dist = distance_from_point(m,b,point[0],point[1])
        
        if this_dist <= min_dist:
            min_dist = this_dist
            px1,py1 = point
                
    print '(',px1,',',py1,') is closest to the line; it is',min_dist,' away'
    return min_dist
	
def line_equation(x0,y0,x1,y1):
    ''' find out what the line equation is between the 2 given points '''
    
    assert (x0, y0) != (x1,y1), 'The two points should not be the same'
    m = (y1 - y0) / (x1 - x0)
    b = y1 - m*x1
    
    print 'y = ',m,'*x + ',b,' is the line connecting the two data points'
    
    return m, b
	
def distance_from_point(m,b,px1,py1):
    ''' given a line equation, find out its distance from the point given '''
    # http://math.ucsd.edu/~wgarner/math4c/derivations/distance/distptline.htm
    
    import math
    
    numerator = py1 - m*px1 - b
    denominator = m**2 + 1
    distance = math.fabs(numerator) / math.sqrt(denominator)
    assert distance >= 0, "The distance must be a positive number"
    
    return distance