import math
import stdio

globalI = 0

def addTwoNumbers(x , y):
	#return x + y
	global globalI
	globalI = x + y

def odd(x):
	return x%2==1

def even(x):
	return x%2==0
			
def main():
	print(globalI)
	addTwoNumbers(5 , 5)
	print(globalI)


main()
print(globalI)
