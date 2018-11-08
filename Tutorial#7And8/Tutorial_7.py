import math
import stdio

def addTwoNumbers(x , y):
	return x + y

def areTheyEqual(x , y ):
	return x == y

def countThePrimes(n):
	for m in range(2 , n):
		print(m)
		for p in range(2 , m):
			if m%p==0 :
				print("Its Divisible!")
			else:
				print("Its Not Divisible!")
			
def main():
	countThePrimes(10)
	
main()
