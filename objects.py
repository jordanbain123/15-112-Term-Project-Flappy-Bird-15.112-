from cmu_graphics import *
from bird import *

class Pipe(object):
    
    def __init__(self, x, app):
        self.x = x
        self.app = app
        self.width = 50
        self.height = random.randint(50, 350)
        self.top = 0
        self.bottom = (self.top + self.height) + 100 #adds a gap between the pipes
        self.color = 'green'
    
    #moves the pipes to the left
    def move(self):
        self.x -= 2

    #make the pipes
    def drawPipes(self):
        drawRect(self.x, self.top, self.x + self.width, self.top + self.height, fill=self.color)
        drawRect(self.x, self.bottom, self.x + self.width, self.app.height, fill=self.color)

    
  

    
    
    