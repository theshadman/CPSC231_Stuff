import stddraw

radius = 0.1
rx = 0.5 # ball x-position
ry = 0.5 # ball y-position
vx = 1.5 # ball x-velocity
vy = 2.3 # ball y-velocity
dt = 0.01
# time step for animation
clicked_on_ball = False


while not clicked_on_ball:
	# check for events and respond accordingly
	if stddraw.mousePressed():
		mx = stddraw.mouseX()
		my = stddraw.mouseY()
		d_squared = (mx-rx)*(mx-rx) + (my-ry)*(my-ry)
		clicked_on_ball = (d_squared < radius * radius)
		
		
	# animate the ball and bounce off walls
	rx += dt * vx
	ry += dt * vy
	if rx < 0.0 or rx > 1.0:
		vx *= -1.0
	if ry < 0.0 or ry > 1.0:
		vy *= -1.0
		
	stddraw.clear()
	stddraw.filledCircle(rx, ry, radius)
	stddraw.show(100.0)
