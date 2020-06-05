import time
import random

from window import Window
from snake import Body
from snake import Head
from fruit import Fruit
from scoreboard import ScoreBoard

class Game():

  # delay to move objects, class attribute
  delay=0.1


  def __init__(self):

    # initialize the objects we are going to need
    self.window=Window() 

    self.body= Body()

    # attaches body to head
    self.head= Head(self.body)

    self.fruit=Fruit()

    self.scoreboard= ScoreBoard()

    # Main gmae loop
    while True:

      # updates the game constantly
      self.window.screen.update()

      # listen for key press
      self.window.screen.listen()

      # treats keypress
      self.window.screen.onkey(self.head.go_up, "Up")
      self.window.screen.onkey(self.head.go_down, "Down")
      self.window.screen.onkey(self.head.go_right, "Right")
      self.window.screen.onkey(self.head.go_left, "Left")  

      self.head.move()

      self.checks_collision()

      time.sleep(self.delay)

#checks  collisions
  def checks_collision(self):

    #checks collision between head and fruit
    if self.head.distance(self.fruit) <15:

     # move the fruit to a random position on screen
      x = random.randint(-370, 370)
      y = random.randint(-290, 290)
      self.fruit.goto(x, y)

     # add new segment to snake's body
      self.head.body.add_segment()

    #  increases score
      self.scoreboard.score+=10
      if self.scoreboard.score > self.scoreboard.top_score:
        self.scoreboard.top_score = self.scoreboard.score
      
        # update score
      self.scoreboard.clear()
      self.scoreboard.write("score: {} top score: {}".format(self.scoreboard.score, self.scoreboard.top_score), align="center", font=("Courier", 24, "normal"))


    
    
    #checks collision between snake and border
    elif self.head.xcor() > 370 or self.head.xcor() < -370 or self.head.ycor() > 290 or self.head.ycor() < -290:

      self.kill_snake()

    # checks collision between snake head and own body
    else:
      for segment in self.head.body.segments:
        if segment.distance(self.head)<20:
          self.kill_snake()



      
  def kill_snake(self):

    time.sleep(0.4)

     # color the snake body in red and stops it
    for segment in self.head.body.segments: 
      segment.direction="stop"
      segment.color("white")
      time.sleep(0.1)
      self.window.screen.update()

    time.sleep(0.3)
    self.head.direction="stop"
    time.sleep(0.3)

    self.head.goto(0,0)

    # hides the segments of the body, only erasing it doesnt clean the drawing, that's why we need to hide
    for segment in self.head.body.segments: 
      segment.hideturtle()

    # reinitializes body segments array
      self.head.body.segments=[]
    
    # resets the score 
    self.scoreboard.score = 0

    # update score
    self.scoreboard.clear()
    self.scoreboard.write("score: {} top score: {}".format(self.scoreboard.score, self.scoreboard.top_score), align="center", font=("Courier", 24, "normal"))

  

game=Game()