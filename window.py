import turtle


class Window():
  def __init__(self):

    self.screen= turtle.Screen()
    self.screen.title("Snake - Simon Games")
    self.screen.bgcolor("#33cc8c")
    self.screen.setup(width=760,height=600)
    self.screen.tracer(0)


   