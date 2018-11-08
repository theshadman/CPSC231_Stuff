import stddraw

radius = 0.5
keep_drawing = True

while keep_drawing:
	stddraw.circle(0.5, 0.5, radius)
	stddraw.show(0.0)
	radius *= 0.8
	response = input("Draw another circle? ")
	keep_drawing = (response == 'y')
