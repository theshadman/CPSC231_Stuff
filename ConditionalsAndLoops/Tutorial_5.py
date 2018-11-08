import math
import stdio

def main():
	#x = int(input("Enter a number: "))
	for i in range(1 , 11):
		for j in range(0 , i):
			stdio.write("*")
		print()

def fibonacci():
	limit = int(input("How many numbers you want?"))
	a = 0
	b = 1
	stdio.write(str(a)+",")
	stdio.write(str(b)+",")
	for i in range(0 , limit):
		c = a + b
		stdio.write(str(c)+",")
		a = b
		b = c
	print()
fibonacci()

#main_while_true()	
#main()

