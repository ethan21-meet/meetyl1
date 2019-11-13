from turtle import Turtle
import turtle
class Ball(Turtle):
	def __init__(self,r,color,dx,dy):
		Turtle.__init__(self)
		self.penup()
		self.r = r
		self.dx = dx
		self.dy = dy
		self.color(color)
		self.shape("circle")
		self.shapesize(r/10)

	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		new_x = current_x +self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy

		right_side_ball = new_x +self.r
		left_side_ball = new_x +self.r
		upper_side_ball = new_y +self.r
		lower_side_ball = new_y +self.r
		self.goto(new_y,new_x)

		if right_side_ball > screen_width:
			new_x = -new_x
		if left_side_ball > screen_width:
			new_x = -new_x 
		if upper_side_ball > screen_height:
			new_y  = -new_y 
		if lower_side_ball > screen_height:
			new_y  = -new_y
		self.goto(new_y,new_x)


screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

ball_1 = Ball(10,"red",10,10)

while 1==1:
	ball_1.move(screen_width,screen_height)












