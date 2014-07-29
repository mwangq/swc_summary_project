from ranges import range_overlap

''' nosetest looks in pwd to find FILES and FUNCTIONS that start with test. nose tests then runs them. nose is greedy, find anything with test in it '''

def test_single_range():
    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
	
	
def test_two_range():
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
	
	
def test_negative_range():
    assert range_overlap([ (0.0, 1.0), (0.0,2.0), (-1.0, 1.0) ]) == (0.0, 1.0)
	
	
def test_no_overlap():
    assert range_overlap([ (0.0, 1.0), (2.0, 3.0) ]) == None
    

def	test_single_point_overlap():
	assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None	
