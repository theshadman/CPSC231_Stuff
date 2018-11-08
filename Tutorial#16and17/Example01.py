

##########################################################
class Person:
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def myfunc(self):
		print("Hello my name is " + self.name)
##########################################################33

p1 = Person("John",25)
p2 = Person("Alice",26)

print(p1.name)
print(p1.age)

p1.myfunc() 

p1.age = 40
print(p1.age)

del p1.age
del p1



mytuple = "apple"
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))













