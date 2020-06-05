import turtle
from turtle import Turtle

class Head(Turtle):

  def __init__(self,body):
    # class Head extends Turtle, to make sure it has all the attributes of Turtle (such as self.direction) we need to initialize Turtle here by calling super.init
    # this is necessary because we overrided turtle init method here to write head init method
    super().__init__()

    # sets normal turtle params
    self.speed(0)
    self.shape("square")
    self.color("black")
    # The function turtle_name.penup() makes sure that the path taken by the snake is not drawn.
    self.penup()
    # centers the head 
    self.goto(0,100)

    # creates attribute direction and sets as stop
    self.direction= "stop"   

    # initializes body even though it is empty
    self.body=body 
  
  def move(self):

    # moves the end segment of the body in reverse order
    for index in range(len(self.body.segments)-1, 0, -1):
      x = self.body.segments[index-1].xcor()
      y = self.body.segments[index-1].ycor()
      self.body.segments[index].goto(x, y)


    #moves the first body segment to the head's position
    if len(self.body.segments)>0:
      x = self.xcor()  #head coord
      y = self.ycor()  #head coord
      self.body.segments[0].goto(x,y)

    # moves the head
    if self.direction == "up":
      y = self.ycor() #y coordinate of the turtle
      self.sety(y + 20)
 
    if self.direction == "down":
      y = self.ycor() #y coordinate of the turtle
      self.sety(y - 20)
 
    if self.direction == "right":
      x = self.xcor() #x coordinate of the turtle
      self.setx(x + 20)
 
    if self.direction == "left":
      x = self.xcor() #x coordinate of the turtle
      self.setx(x - 20)
    


  def go_up(self):
    if self.direction != "down":
        self.direction = "up"
  
  def go_down(self):
    if self.direction != "up":
        self.direction = "down"
  
  def go_right(self):
    if self.direction != "left":
       self.direction = "right"
  
  def go_left(self):
    if self.direction != "right":
        self.direction = "left"


class Body():
  def __init__(self):
    # initialize array that will group body segments
    self.segments=[]

  def add_segment(self):
    segment=turtle.Turtle()
    segment.speed(0)
    segment.shape("square")
    segment.color("#a67c58")
    segment.penup()
    segment.goto(1000,1000) #hides the segment so it doesnt appear in the center of the screen

  # adds segment to body
    self.segments.append(segment)

  


