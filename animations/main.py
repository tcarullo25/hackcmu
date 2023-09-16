from cmu_graphics import *
from utils import *
from PIL import Image
import math
import random


def getPlanetData():
    import sys
    sys.path.insert(1, '../data')
    from scrapePlanets import planetData
    return planetData()


def onAppStart(app):
    app.onSplashScreen = True

    app.planets = getPlanetData()
    for planet in app.planets:
        planet.theta = random.randint(0, 47) / 15

    app.distances = [20, 50, 80, 110, 220, 280, 330, 380, 430]
    app.planetColors = ['gray', 'darkRed', 'blue', 'red',
                        'orange', 'gold', 'skyBlue', 'mediumBlue', 'gray']
    app.planetLabel = None
    app.px, app.py = None, None

    app.rocketImage = Image.open('rocket.png')
    app.rocketImage = CMUImage(app.rocketImage)
    app.rocketAngle = 45

    app.scaleView = False
    app.paused = False

    app.smallHover = False
    app.largeHover = False
    app.sunHover = False


def onKeyPress(app, key):
    if key == 'space':
        app.paused = not app.paused
    if key == 's':
        for planet in app.planets:
            planet.dTheta /= 1.5
    if key == 'f':
        for planet in app.planets:
            planet.dTheta *= 1.5


def onStep(app):
    if not app.paused:
        for planet in app.planets:
            planet.moveStep()


def onMouseMove(app, mouseX, mouseY):
    if 870 <= mouseX <= 900 and 750 <= mouseY <= 780:
        app.smallHover = True
    else:
        app.smallHover = False
    if 920 <= mouseX <= 950 and 750 <= mouseY <= 780:
        app.largeHover = True
    else:
        app.largeHover = False
    if distance(mouseX, mouseY, app.width / 2, app.height / 2) < 20:
        app.sunHover = True
        return
    else:
        app.sunHover = False

    if app.paused:
        for i in range(len(app.planets)):
            planet = app.planets[i]
            px, py = polarToRectangular(app, app.distances[i], planet.theta)
            if distance(mouseX, mouseY, px, py) < 20:
                app.px, app.py = px, py
                app.planetLabel = planet.planet
                return
            else:
                app.px, app.py = None, None
                app.planetLabel = None


def onMousePress(app, mouseX, mouseY):
    if 870 <= mouseX <= 900 and 750 <= mouseY <= 780:
        app.scaleView = True
    if 920 <= mouseX <= 950 and 750 <= mouseY <= 780:
        app.scaleView = False
    if app.width//3 + 25 <= mouseX <= 670 and 515 <= mouseY <= 555:
        app.onSplashScreen = False

def drawSplashScreen(app):
    drawRect(0,0,app.width,app.height,fill='darkBlue')
    drawLabel('Space Navigate', app.width//2, app.height//4 + 50, size = 40,font = 'arial', fill = 'black')
    drawLabel('By: Tim Carullo, Sam Chen, Ethan Kwong, and Jieun Lim', app.width*3//8 - 40, app.height*7//8 + 80, size = 26, fill = 'white')
    for i in range(len(app.planets)):
        color = app.planetColors[i]

        # Orbit path
        drawCircle(app.width/2, app.height/2,
                   app.distances[i], fill=None, border=color, borderWidth=1)
    drawRect(app.width//3 + 25, 515,  app.width*5//16, 40, fill='gray', border='white')
    drawLabel("Start", 500, 535, bold= True, fill = 'green', size = 30)

def redrawAll(app):
    if app.onSplashScreen:
        drawSplashScreen(app)
    else:
        drawRect(0, 0, app.width, app.height, fill="black")
        # Planets
        drawPlanets(app)
        # Sun
        drawSun(app)
        drawScaleButtons(app)
        drawRocket(app)
        drawLabels(app)


def drawLabels(app):
    if app.planetLabel is not None:
        drawRect(app.px - 50, app.py - 40, 100,
                 30, fill='gray', border='white')
        drawLabel(app.planetLabel, app.px, app.py - 25, size=16, fill='white')
    elif app.sunHover:
        drawRect(400, 340, 200, 40, fill='gray', border='white')
        drawLabel('Sun is not to scale', 500, 360, size=16, fill='white')
    elif app.smallHover:
        drawRect(830, 700, 110, 40, fill='gray', border='white')
        drawLabel('To scale size', 885, 720, size=16, fill='white')
    elif app.largeHover:
        drawRect(880, 700, 110, 40, fill='gray', border='white')
        drawLabel('To view size', 935, 720, size=16, fill='white')


def drawRocket(app):
    drawImage(app.rocketImage, app.width/2, app.height /
              2, align='center', rotateAngle=app.rocketAngle, width=30, height=30)


def drawSun(app):
    drawCircle(app.width/2, app.height/2, 10, fill="yellow")


def drawPlanets(app):
    for i in range(len(app.planets)):
        planet = app.planets[i]
        radius = max(planet.diameter / 9000,
                     2) if app.scaleView else math.sqrt(planet.diameter) / 15
        dFromSun, theta = app.distances[i], planet.theta
        cx, cy = polarToRectangular(app, dFromSun, theta)
        color = app.planetColors[i]

        # Orbit path
        drawCircle(app.width/2, app.height/2,
                   app.distances[i], fill=None, border=color, borderWidth=1)

        # Planet
        drawCircle(cx, cy, radius, fill=color)


def drawScaleButtons(app):
    smallBorder = "white" if app.smallHover else None
    largeBorder = "white" if app.largeHover else None

    drawRect(870, 750, 30, 30, fill='gray', border=smallBorder)
    drawLabel('_', 885, 762, fill='white', size=24, bold=True)
    drawRect(920, 750, 30, 30, fill='gray', border=largeBorder)
    drawLabel('+', 935, 765, fill='white', size=24)


def main():
    runApp(width=1000, height=800)


main()
