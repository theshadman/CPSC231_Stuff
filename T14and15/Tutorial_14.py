#from tkinter import*
import tkinter as tk
import time
'''
animation = Tk()
canvas = Canvas(animation, width=500, height=500)
canvas.pack()
canvas.create_line(50,50,150,150)

while True:
	for x in range(50):
		canvas.move(1,5,0)
		animation.update()
		time.sleep(0.05)

	for x in range(50):
		canvas.move(1,-5,0)
		animation.update()
		time.sleep(0.05)
'''
	

		

global switch
switch = 1

win = tk.Tk()

win.title("Python GUI")

win.geometry("500x500")

win.resizable(False, False)

label = tk.Label(win, text="A Label")
label.grid(column=0, row=0)

#buttons
def clicked_01():
	switch = int(input("? "))
	button_1.configure(text="I have been clicked")
	if switch%2==0:		
		label.configure(foreground = 'red')
		label.configure(text="a red line")
	else:
		label.configure(foreground = 'blue')
		label.configure(text="a blue line")
	switch+=1
	
def clicked_02():
	label.configure(text='Hello '+name.get())

#textBox
name = tk.StringVar()
textBox_1 = tk.Entry(win, width=12, textvariable=name)
textBox_1.grid(column=0,row=1)

button_1 = tk.Button(win, text="I dare you, I double dare you.",command=clicked_01)
button_1.grid(column=1, row=0)

while int(input("? "))%2==0:
	clicked_01()

win.mainloop()























