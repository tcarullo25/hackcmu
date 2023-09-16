class Planet:
    def __init__(self, planet, mass, diameter, gravity, rotPeriod, v, period, dist):
        self.planet = planet
        self.mass = mass
        self.diameter = int(diameter.replace(',', ''))
        self.gravity = gravity
        self.rotPeriod = rotPeriod
        self.orbitalVelocity = v
        self.orbitalPeriod = period
        dist = dist[:-1] if dist[-1] == '*' else dist
        self.dist = int(float(dist))
        self.color = None
