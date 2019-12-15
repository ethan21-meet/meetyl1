users=[]
Posts=[]

class User(object):
	def __init__(self,name,email,password,):
		
		
		self.name = name
		self.email = email
		self.password = password
		self.friends_list =[]
		self.posts = []
		



	def add_friends (self,email):
		self.friends_list.append(email)
		print(self.name + " has added " + email + " as your friend")

	def remove_friend (self,email):
		self.friends_list.remove(email)
		print( self.name + " has removed " + email + " as a friend")
	

	def post(self,text):
		posst = Post(text, 0, 0, self.email)
		self.posts.append(posst)
		print(self.name + " has posted " + text)

	def get_userInfo(self):
		print("Name:" + self.name + "Email:" + self.email + "Password:" + self.password + "Friends:" + str(self.friends_list))


user1= User("josh" , "joshi8@meet.mit.edu" ,"helloooo"  )
user2 = User("andres" ,"andresini@meet.mit.edu" ,"liverpool" )


user1.get_userInfo()

class Post(object):
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


class Comment(Post):
	def __init__(self,like,text,emoji,num_comments):
		self.like = 0
		self.emoji = emoji
		self.text = text
		self.num_comments = 0

	def like(self,text):
		self.like = self.like + 1
		print ("someone liked your comment!")

	def num_comments(self,text):
		self.num_comments = self.num_comments + 1
		print("someone commented on your comment")


while True:
	x=input("log in - 1 sign up - 2")
	if x==1:
		print("log in mate")
		email = input("what is your email?")
		password = input("what is your password")
		print("you logged in")
		for user in users:
			if email== loggedin.email and password == loggedin.password:

				
				print("you logged in")
			if email != loggedin.email and password == loggedin.password:
				print("youre wrong!")

				while 0==0:
					q = input("what do you want to do?")
					if q == "comment":
						Posts[0].add_comments
						print("you added a comment!")
						if q == "like":
							Posts[0].add_likes
							print("you added a like!")
						if q == "add_friends":
							k=input('freinds name')

							loggedin.add_friends(k)






				
						
	
	if x==2:
		 y= input("whats your name?")
		 z= input("whats your email")
		 a= input("whats your password?")
		 print("you signd up!")
		 loggedin = User(y,z,a)
















		


	 






