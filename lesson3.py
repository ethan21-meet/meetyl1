class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
			self.sound = sound
			self.name = name
			self.age = age
			self.favorite_color = favorite_color
	def eat(self,food):
			print("Yummy!! " + self.name + " is eating " + food)
	def description(self):
			print(self.name + " is " + str(self.age) +" years old and loves the color "+self.favorite_color)
	def make_sound(self):
		for ani in range(3):
			print(self.sound)
animal1 = Animal("moooooooooo", "cow", 10, "white")
animal1.eat("grass")
animal1.description()
animal1.make_sound()



class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat_breakfast(self, breakfast):
		print(self.name + " is eating" + breakfast)
person1 = Person("Emily",17, "New York", "Female")
person1.eat_breakfast(" omlet ")

class Bird(object)
	def __init__(self,name,color,speed)
		self.name = name
		self.color = color
		self.speed = speedss

