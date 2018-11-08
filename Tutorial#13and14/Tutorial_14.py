import tkinter

def main(i):
	top = tkinter.Tk()
	C = tkinter.Canvas(top, bg="grey",height=300,width=300)
	line = C.create_line(0,150,20,150)
	C.pack()
	top.mainloop()

for i in range(5):
	main(i)

