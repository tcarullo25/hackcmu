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
    app.planets = getPlanetData()
    for planet in app.planets:
        planet.theta = random.randint(0, 47) / 15

    app.distances = [20, 50, 80, 110, 220, 280, 330, 380, 430]
    app.planetColors = ['gray', 'darkRed', 'blue', 'red',
                        'orange', 'gold', 'skyBlue', 'mediumBlue', 'gray']

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
    else:
        app.sunHover = False


def onMousePress(app, mouseX, mouseY):
    if 870 <= mouseX <= 900 and 750 <= mouseY <= 780:
        app.scaleView = True
    if 920 <= mouseX <= 950 and 750 <= mouseY <= 780:
        app.scaleView = False


def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill="black")
    # Planets
    drawPlanets(app)
    # Sun
    drawSun(app)
    drawScaleButtons(app)
    drawRocket(app)


def drawRocket(app):
    drawImage(app.rocketImage, app.width/2, app.height /
              2, align='center', rotateAngle=app.rocketAngle, width=30, height=30)


def drawSun(app):
    drawCircle(app.width/2, app.height/2, 10, fill="yellow")

    if app.sunHover:
        drawRect(400, 340, 200, 40, fill='gray', border='white')
        drawLabel('Sun is not to scale', 500, 360, size=16, fill='white')


def drawPlanets(app):
    for i in range(len(app.planets)):
        planet = app.planets[i]
        radius = max(planet.diameter / 9000,
                     2) if app.scaleView else math.sqrt(planet.diameter) / 15
        distance, theta = app.distances[i], planet.theta
        cx, cy = polarToRectangular(app, distance, theta)
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

    if app.smallHover:
        drawRect(830, 700, 110, 40, fill='gray', border='white')
        drawLabel('To scale size', 885, 720, size=16, fill='white')

    if app.largeHover:
        drawRect(880, 700, 110, 40, fill='gray', border='white')
        drawLabel('To view size', 935, 720, size=16, fill='white')


def main():
    runApp(width=1000, height=800)


main()
