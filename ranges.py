def range_overlap(ranges):
    ''' This code returns the range that overlaps among the submitted sets of (low, high) tuple ranges '''
    
    # good principle in programming: initialize from data, don't initialize from scratch
    lowest = ranges[0][0]
    highest = ranges[0][1]
    
    # can extract each tuple as a set of low, high
    for (low, high) in ranges:
        highest = min(highest, high)
        lowest = max(lowest, low)
    
    # if lower is higher than highest, return None
    if lowest >= highest:
        return None
    else:    
        return (lowest, highest)