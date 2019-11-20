users=[]
Posts=[]

class User(object):
	def __init__(self,name,email,password,):
		
		
		self.name = name
		self.email = email
		self.password = password
		self.friends_list =[]
		



	def add_friends (self,email):
		self.friends_list.append(email)
		print(self.name + " has added " + email + " as your friend")

	def remove_friend (self,email):
		self.friends_list.remove(email)
		print( self.name + " has removed " + email + " as a friend")
	

	def post(self,text):
		posst = Post(text, 0, 0, self.email)
		posts.append(posst)
		print(self.name + " has posted " + text)

	def get_userInfo(self):
		print("Name: ["+self.name+"] "+ "Email:["+self.email+"] "+ "Password:["+self.password+"] "+ "Friends:["+str(self.friends_list))


user1= User("josh" , "joshi8@meet.mit.edu" ,"helloooo"  )
user2 = User("andres" ,"andresini@meet.mit.edu" ,"liverpool" )


user1.get_userInfo()

class post(object):
	def __init__(self,text,num_likes,num_comments,author):
		self.num_likes = 0
		self.num_comments = 0
		self.text = text
		self.author = author
	
	def add_likes(self):
		self.num_likes = self.num_likes + 1

		print("i liked this post!!")

	def add_comments(self):
		self.num_comments = self.num_comments + 1
user1.post("hi hello")
user1.get_userInfo()







		


	 






