import math
import stdio
from array import *


def bubble():
	arr = [5,8,4,3]
	for i in range(len(arr)-1):
		for j in range(len(arr)-i):
			if arr[i]>arr[i+j]:
				temp = arr[i]
				arr[i]=arr[i+j]
				arr[i+j]=temp
	print(arr)

def selection():
	arr = [5,8,4,3]
	sortedArr = [arr[0]]
	for i in range(1,len(arr)):
		print(sortedArr)
		insert = False
		for j in range(len(sortedArr)):
			if arr[i] < arr[j]:
				sortedArr.insert(j,arr[i])
				insert = True
				break
		if insert:
			pass
		else:
			sortedArr.append(arr[i])
	print(sortedArr)

def twoDArrays():
	arr2d = [[ 5 , 6] , [0 , 8] , [1 , 7]]
	#print(arr2d)
	#print(arr2d[0])
	#print(arr2d[0][0])
	
	'''
	Iterating through a 2D array.
	
	for row in arr2d:
		for col in row:
			print(col , end = ",")
		print()
	'''
	
	'''
	Changing values in a traditional way
	Updating values.
	
	arr2d[0] = [10 , 20]
	#arr2d[1][0] = 88
	print(arr2d)
	'''
	'''
	inserting values
	'''
	arr2d[0].insert(1, 444)
	print(arr2d)
	
	'''
	Deleting
	'''
	'''del arr2d[2]
	print(arr2d)
	'''

twoDArrays()
