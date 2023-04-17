from cmu_graphics import *
from bird import *
from objects import *


def onAppStart(app):
    #set up game window
    app.title = "Flappy Bird 15.112!"
    app.instructions = 'Press space to start'
    app.width = 500
    app.height = 550
    url = 'http://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Kangaroo_MusiQue_-_The_Neverwritten_Role_Playing_Game.mp3'
    app.sound = Sound(url)
    app.url = 'https://wallpapercave.com/wp/wp6957163.png'
    
    #add bird

    #game objects
    app.score = 0
    app.gameOver = False
    app.bird = Bird(app, 250, 100)
    app.pipes = []
    app.passed = False
    

    

def redrawAll(app):
    
    #Setting up the background, title, and instructions
    drawImage(app.url, 125, 200, align='center')
    drawLabel(app.title, 250, 75, size=40, bold=True, fill='lightgreen', border='black')

    drawLabel(app.instructions, 250, 120, size=25, bold=True)
'''
    #game objects
    for pipe in app.pipes:
       pipe.drawPipes(app) 
      
    app.bird.drawBird(app)

    drawLabel(str(app.score), app.width//2, app.height//5, fill='white')

    if app.gameOver == True:
       drawLabel('Game Over', app.width//2, app.height//2, fill='red')
'''


    
  
  
 
    


   


def onKeyPress(app, key):
   if key == 'space':
      app.sound.play(loop=True)
  

    

def main():
  runApp()

main()

