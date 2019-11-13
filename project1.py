class User(object):
	def __init__(self,name,email,password,friends_list,posts):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = []
		self.post = []

	def add_friends (self,email):
		friends_list.append(email)
		print(self.name + "has added" + email + "as a friend")

	def remove_friend (self,email):
		friends_list.remove(email)
		print( self.name + "has removed" + email + "as a friend")

	def post(self,text):

		post.append(text)
		print(self.name + "has posted" + text)

	def get_userInfo(self):
		print("Name: ["+self.name+"] "+ "Email:["+self.email+"] "+ "Password:["+self.password+"] "+ "Friends:["+str(self.friends_list)+"])"+"Posts:["+str(self.post)+"]")


user1 = User("josh","joshi8@meet.mit.edu","helloooo")
user2 = User("andres","andresini@meet.mit.edu","liverpool")
user1.add_friends("andresini@meet.mit.edu")
user1.post("i love my best friends")

user1.get_userInfo()
user2.get_userInfo()
user1.remove_friend("andresini@meet.mit.edu")
