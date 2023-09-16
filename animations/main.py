from cmu_graphics import *
import math


def getPlanetData():
    import sys
    sys.path.insert(1, '../data')
    from scrapePlanets import planetData
    return planetData()


def onAppStart(app):
    app.planets = getPlanetData()


def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill="black")

    # Sun
    drawCircle(app.width/2, app.height/2, 10, fill="yellow")
    for planet in app.planets:
        # radius = math.sqrt(planet.diameter) / 15
        radius = planet.diameter / 9000
        cx, cy = app.width/2 - (planet.dist / 8), app.height/2
        print(cx, cy, radius)
        drawCircle(cx, cy, radius, fill="white")


def main():
    runApp(width=1000, height=800)


main()
