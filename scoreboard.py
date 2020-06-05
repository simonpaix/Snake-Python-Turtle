import turtle
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
    # class Pen extends Turtle, to make sure it has all the attributes of Turtle  we need to initialize Turtle here by calling super.init
    # this is necessary because we overrided turtle init method here to write pen init method
      super().__init__()

      self.speed(0)
      self.shape("square")
      self.color("black")
      self.penup()
      self.hideturtle()
      self.goto(0, 260)

      # score and top score 
      self.score = 0
      self.top_score = 0
      self.write("Score: 0 top score: {}".format(self.top_score), align="center", font=("Courier", 24, "normal"))

   
