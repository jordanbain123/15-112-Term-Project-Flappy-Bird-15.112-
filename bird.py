from  cmu_graphics import *

class Bird(object):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.velocity = 0
        self.gravity = 0.5
        
    
    def jump(self):
        self.velocity = -10
    
    def move(self):
       #increases the velocity
        self.velocity += self.gravity 
        #updates the position
        self.y += self.velocity
    
    def drawBird(self, canvas):
        #draws the yellow cirlce (the bird)
        canvas.create_oval(self.x - self.size/2, self.y - self.size/2,
                 self.x + self.size/2, self.y + self.size/2,
                 fill='yellow')
            

    
   