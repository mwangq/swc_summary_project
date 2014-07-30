import summary
import numpy

def test_line_equation():
	assert summary.line_equation(0,0,1,1) == (1,0)

	
def test_distance_from_point():
	assert summary.distance_from_point(1,0,1,1) == 0

	
def test_closest_point():
	assert summary.closest_point(0,0,1,1,numpy.array([[1,1]])) == 0