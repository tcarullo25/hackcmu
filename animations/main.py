from cmu_graphics import *
from utils import *
from PIL import Image
from UI import *
import math
import random


def getPlanetData():
    import sys
    sys.path.insert(1, '../data')
    from scrapePlanets import planetData
    return planetData()


def initPlanets(app):
    app.planets = getPlanetData()
    distances = [20, 50, 80, 110, 220, 280, 330, 380, 430]
    colors = ['gray', 'darkRed', 'blue', 'red',
              'orange', 'gold', 'skyBlue', 'mediumBlue', 'gray']
    app.planetDict = dict()
    for i in range(len(app.planets)):
        planet = app.planets[i]
        app.planetDict[planet.planet] = (planet, distances[i], colors[i])
        planet.theta = random.randint(0, 47) / 15

    app.planetLabel = None
    app.px, app.py = None, None
    app.startPlanet, app.endPlanet = None, None


def initRocket(app):
    app.rocketImage = Image.open('rocket.png')
    app.rocketImage = CMUImage(app.rocketImage)
    app.bg = Image.open('background.jpg')
    app.bg = CMUImage(app.bg)
    app.rocketAngle = 45
    app.rx, app.ry = None, None


def onAppStart(app):
    app.onSplashScreen = True
    initPlanets(app)
    initRocket(app)
    initStar(app)

    app.scaleView = False
    app.paused = False

    app.smallHover = False
    app.largeHover = False
    app.sunHover = False
    app.toggleBackground = False
    app.steps = 0


def getRocketInputs(app):
    app.paused = True

    start = app.getTextInput("Choose a starting planet")
    while start.upper() not in app.planetDict:
        start = app.getTextInput("Please choose a valid planet")
    end = app.getTextInput("Choose an ending planet")
    while end.upper() not in app.planetDict:
        end = app.getTextInput("Please choose a valid planet")
    app.startPlanet, app.endPlanet = app.planetDict(start), app.planetDict(end)


def onKeyPress(app, key):
    if not app.onSplashScreen:
        if key == 'space':
            app.paused = not app.paused
        if key == 's':
            for planet in app.planets:
                planet.dTheta /= 1.5
        if key == 'f':
            for planet in app.planets:
                planet.dTheta *= 1.5
        if key == 'm':
            getRocketInputs(app)
            app.rx, app.ry = polarToRectangular()
        if key == 't':
            app.toggleBackground = not app.toggleBackground


def onStep(app):
    if not app.paused:
        app.steps += 1
        for planet in app.planets:
            planet.moveStep()
        if app.toggleBackground and (app.steps % 7 == 0):
            updateStar(app)


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
        for planet in app.planetDict:
            planet, orbitDistance, color = app.planetDict[planet]
            px, py = polarToRectangular(app, orbitDistance, planet.theta)
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
    if app.width//3 + 15 <= mouseX <= 660 and 515 <= mouseY <= 555:
        app.onSplashScreen = False


def drawSplashScreen(app):
    drawImage(app.bg, app.width/2, app.height /
              2, align='center', width=app.width, height=app.height)
    drawLabel('Space Navigate', app.width//2, app.height//4 + 250, size = 40,font = 'arial', fill = 'white')
    drawLabel('By: Tim Carullo, Sam Chen, Ethan Kwong, and Jieun Lim', app.width*3//8 - 40, app.height*7//8 + 80, size = 26, fill = 'white')
    drawRect(app.width//3 + 15, 515,  app.width*5//16, 40, fill='gray', border='white')
    drawLabel("Start", 500, 535, bold= True, fill = 'white', size = 30)

def redrawAll(app):
    if app.onSplashScreen:
        drawSplashScreen(app)
    else:
        if app.toggleBackground:
            drawStars(app)
        else:
            drawRect(0, 0, app.width, app.height, fill="black")
        drawPlanets(app)
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
    if app.rx is not None and app.ry is not None:
        drawImage(app.rocketImage, app.rx, app.ry, align='center',
                  rotateAngle=app.rocketAngle, width=30, height=30)


def drawSun(app):
    drawCircle(app.width/2, app.height/2, 10, fill="yellow")


def drawPlanets(app):
    for planet in app.planetDict:
        planet, orbitDistance, color = app.planetDict[planet]
        radius = max(planet.diameter / 9000,
                     2) if app.scaleView else math.sqrt(planet.diameter) / 15
        dFromSun, theta = orbitDistance, planet.theta
        cx, cy = polarToRectangular(app, dFromSun, theta)

        # Orbit path
        drawCircle(app.width/2, app.height/2,
                   orbitDistance, fill=None, border=color, borderWidth=1)

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
