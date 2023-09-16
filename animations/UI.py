from cmu_graphics import *
import random
import math
from PIL import Image


class Star:
    def __init__(self, x, y, radius, angle):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle


def initStar(app):
    app.deathTime = random.randint(50, 100)
    app.curAngle = 1
    app.starList = []
    app.universe = CMUImage(Image.open('night1.jpg'))


def createStar(app):
    newX = random.randint(20, 480)
    newY = random.randint(20, 480)
    newR = random.randint(1, 3)
    newA = random.randint(2, 50)
    app.starList.append(Star(newX, newY, newR, newA))


def drawStar(app, x, y, r):
    drawCircle(x, y, r, fill="white")


def updateStar(app):
    createStar(app)
    app.curAngle += 1
    app.deathTime -= 1
    for star in app.starList:
        star.angle += 1
        star.x = star.x + (app.width//star.radius) * math.cos(star.angle)
        star.y = star.y + (app.width//star.radius) * math.sin(star.angle)
    if app.deathTime == 0:
        app.starList.pop()


def drawStars(app):
    new = app.universe.image

    drawCircle(app.width/2, app.height/2, app.width/2)
    drawImage(app.universe, 0, 0, align="center",
              width=new.width*100,
              height=new.height*80,
              rotateAngle=app.curAngle)
    for star in app.starList:
        drawStar(app, star.x, star.y, star.radius)
