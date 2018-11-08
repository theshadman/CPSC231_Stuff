import math
import stdio

def takeInputFromFile():
	'''
	Reading the file.
	Puts each line in an array called lines (bad name)
	'''
	input_file = open('inputs.txt')	
	lines = input_file.readlines()
	input_file.close()
	
	'''
	What is lines array/list?
	'''
	
	print("The lines are as follows: ")
	for i in range(len(lines)):
		if i%2==1:
			lines_wo_commas = lines[i].rstrip()
			elements = lines_wo_commas.split(',')
			name = elements[0]
		identity = elements[1]
		age = elements[2]
		#print('Line: ', i , ' has elements\n [0] = ' , name, '\n [1] = ', identity , '\n [2]= ',age)
		
		
		'''
		Output to a file...
		'''
		output_file = open('output.txt' , 'w')
		output_file.write('This is the first line. Ignore this.\n')
		for i in range(len(lines)):
			output_line = '[0]=' + elements[0]+ ' [1] = ' + elements[1] + '\n'
			output_file.write(output_line)
		output_file.close()
		
	

def main():
	takeInputFromFile()
	

def takeInputFromFile():
	'''
	Reading the file.
	Puts each line in an array called lines (bad name)
	'''
	input_file = open('inputs.txt')	
	lines = input_file.readlines()
	input_file.close()
	
	'''
	What is lines array/list?
	'''
	
	print("The lines are as follows: ")
	for i in range(len(lines)):
		lines_wo_commas = lines[i].rstrip()
		elements = lines_wo_commas.split(',')
		name = elements[0]
		identity = elements[1]
		age = elements[2]
		#print('Line: ', i , ' has elements\n [0] = ' , name, '\n [1] = ', identity , '\n [2]= ',age)
		
		
		'''
		Output to a file...
		'''
		output_file = open('output.txt' , 'w')
		output_file.write('This is the first line. Ignore this.\n')
		for i in range(len(lines)):
			output_line = '[0]=' + elements[0]+ ' [1] = ' + elements[1] + '\n'
			output_file.write(output_line)
		output_file.close()
		
	

main()
