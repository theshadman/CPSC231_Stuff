import stddraw
import random as rand
import time,math
import stddraw

board_configuration = [[]]
turn = 1
def update_board(x,y,z):
	find_real_xy()
	board_configuration[x][y]=z
	
def draw_board():
	for x in range(_):
		for y in range(_):
			draw_rectangle if board_configuration[x][y]==0
			draw_filled_rectangle if board_configuration[x][y]==1

def run_game():
	global turn
	while not game_end():
		if mouse_clicked():
			x_coord_mouse = get_X()
			y_coord_mouse = get_Y()
			if turn is odd:
				update_board(x_coord_mouse, y_coord_mouse,1)
			else:
				update_board(x_coord_mouse, y_coord_mouse,2)			
			turn+=1

		stddraw.clear()
		draw_board()
		stddraw.show(400.0)
	
	
	

run_game()






































'''
click_x=[]
click_y=[]

def drawbox_filled(x,y):
	stddraw.filledRectangle(x,y,0.099,0.099)

def drawbox(x,y):
	stddraw.rectangle(x,y,0.1,0.1)

def create_board():
	for y in range(10):
		y_coord = y/10
		for x in range(10):
			x_coord = x/10	
			drawbox(x_coord,y_coord)
	for index in range(len(click_x)):
		drawbox_filled(click_x[index],click_y[index])
	

def start_game():
	global click_x,click_y
	while True:
		mouse_x = 1.1
		mouse_y = 1.1
		t=False
		if stddraw.mousePressed():
			mouse_x = math.floor(stddraw.mouseX()*10)/10
			mouse_y = math.floor(stddraw.mouseY()*10)/10
			click_x.append(mouse_x)
			click_y.append(mouse_y)
			t=True
		stddraw.clear()
		create_board()
		stddraw.show(100.0)

create_board()
start_game()
'''
