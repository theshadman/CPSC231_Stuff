import stddraw
import random as rand
import time

radius = 0.1
rx = 0.5 # ball x-position
ry = 0.5 # ball y-position
vx = 0.5 # ball x-velocity
vy = 1.3 # ball y-velocity
dt = 0.01 # time step for animation
clicked_on_ball = False

def drawbox(x,y):
	stddraw.rectangle(x,y,0.1,0.1)

def draw_box_block(x,y):
	drawbox(x,y)
	drawbox(x+0.1,y)
	drawbox(x,y+0.1)
	drawbox(x+0.1,y+0.1)

def collision_check(y):
	return y>0


while True:
	shape = 1
	#boxShape
	if shape==1:
		x=rand.randint(1,8)/10
	else:
		x=rand.randint(1,8)/10

	y=1.0
	decrement=0.1
	#falling effect
	while collision_check(y):
		y-=decrement
		stddraw.clear()
		draw_box_block(x,y)
		stddraw.show(400.0)


'''
# animate the ball and bounce off walls
	rx += dt * vx
	ry += dt * vy
	if rx < 0.0 or rx > 1.0:
		vx *= -1.0
	if ry < 0.0 or ry > 1.0:
		vy *= -1.0
	stddraw.clear()
	stddraw.filledCircle(rx, ry, radius)
	stddraw.show(1000.0 * dt)
'''

'''
a=0.5
b=1.0
while b>0:
	b-=0.05
	stddraw.clear()
	draw_box_block(a,b)
	stddraw.show(400.0)
'''