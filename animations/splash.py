from cmu_graphics import *
from PIL import Image


def drawInfoScreen(app):
    sub = app.bkground.image
    drawImage(app.bkground, 0, 0, align="center",
              width=sub.width*100,
              height=sub.height*80)
    drawLabel("Check out a part of our universe!",
              app.width//2, app.height//2, fill="white",
              font='Arial', size=25)
    drawLabel("Make sure to press 't' to see the stars!",
              app.width//2, app.height//2 - 40, fill="white",
              font='Arial', size=25)
    drawLabel("Press g to continue your journey:)",
              app.width//2, app.height//2 - 80, fill="white",
              font='Arial', size=25)
