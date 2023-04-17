from cmu_graphics import *

#testing to make sure cmu_graphics have been imported properly into my folder
def onAppStart(app):
    app.url = 'https://academy.cs.cmu.edu/static/media/project_10.472f439f.jpg'

def redrawAll(app):
    imageWidth, imageHeight = getImageSize(app.url)

    drawLabel(f'Original ({imageWidth}x{imageHeight})', 125, 75, size=16)
    drawImage(app.url, 125, 200, align='center')

    drawLabel('Half-sized', 325, 75, size=16)
    drawImage(app.url, 325, 200, align='center',
              width=imageWidth//2, height=imageHeight//2)

def main():
  runApp()

main()