import math


class Planet:
    def __init__(self, planet, mass, diameter, gravity, rotPeriod, oVelo, period, dist):
        self.planet = planet
        self.mass = mass
        self.diameter = int(diameter.replace(',', ''))
        self.gravity = gravity
        self.rotPeriod = rotPeriod
        self.orbitalVelocity = float(oVelo)
        self.orbitalPeriod = period
        dist = dist[:-1] if dist[-1] == '*' else dist
        self.dist = int(float(dist))
        self.theta = 0
        self.orbitDistance = 2 * math.pi * self.dist

        # Move a little slower to make it more visually appealing
        self.dTheta = self.orbitalVelocity / self.orbitDistance * math.pi

    def moveStep(self):
        self.theta = (self.theta + self.dTheta) % (2 * math.pi)
