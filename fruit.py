import turtle
from turtle import Turtle

# Fruit that the snake loves to eat
class Fruit(Turtle):
  def __init__(self):
    # class Fruit extends Turtle, to make sure it has all the attributes of Turtle  we need to initialize Turtle here by calling super.init
    # this is necessary because we overrided turtle init method here to write fruit init method
    super().__init__()
    self.speed(0)
    self.shape("circle")
    self.color("red")
    self.penup()
    self.shapesize(0.50, 0.50)
    self.goto(0, 0)
