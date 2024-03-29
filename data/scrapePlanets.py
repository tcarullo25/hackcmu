import sys
import requests
from bs4 import BeautifulSoup


TESTING = True


def transpose(matrix):
    result = []
    rows, cols = len(matrix), len(matrix[0])
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result


DATA = [['', 'Mass (1024kg)', 'Diameter (km)', 'Density (kg/m3)', 'Gravity (m/s2)', 'Escape Velocity (km/s)', 'Rotation Period (hours)', 'Length of Day (hours)', 'Distance from Sun (106 km)', 'Perihelion (106 km)', 'Aphelion (106 km)', 'Orbital Period (days)', 'Orbital Velocity (km/s)', 'Orbital Inclination (degrees)', 'Orbital Eccentricity', 'Obliquity to Orbit (degrees)', 'Mean Temperature (C)', 'Surface Pressure (bars)', 'Number of Moons', 'Ring System?', 'Global Magnetic Field?', ''], ['MERCURY', '0.330', '4879', '5429', '3.7', '4.3', '1407.6', '4222.6', '57.9', '46.0', '69.8', '88.0', '47.4', '7.0', '0.206', '0.034', '167', '0', '0', 'No', 'Yes', 'MERCURY'], ['VENUS', '4.87', '12,104', '5243', '8.9', '10.4', '-5832.5', '2802.0', '108.2', '107.5', '108.9', '224.7', '35.0', '3.4', '0.007', '177.4', '464', '92', '0', 'No', 'No', 'VENUS'], ['EARTH', '5.97', '12,756', '5514', '9.8', '11.2', '23.9', '24.0', '149.6', '147.1', '152.1', '365.2', '29.8', '0.0', '0.017', '23.4', '15', '1', '1', 'No', 'Yes', 'EARTH'], ['MOON', '0.073', '3475', '3340', '1.6', '2.4', '655.7', '708.7', '0.384*', '0.363*', '0.406*', '27.3*', '1.0*', '5.1', '0.055', '6.7',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '-20', '0', '0', 'No', 'No', 'MOON'], ['MARS', '0.642', '6792', '3934', '3.7', '5.0', '24.6', '24.7', '228.0', '206.7', '249.3', '687.0', '24.1', '1.8', '0.094', '25.2', '-65', '0.01', '2', 'No', 'No', 'MARS'], ['JUPITER', '1898', '142,984', '1326', '23.1', '59.5', '9.9', '9.9', '778.5', '740.6', '816.4', '4331', '13.1', '1.3', '0.049', '3.1', '-110', 'Unknown*', '92', 'Yes', 'Yes', 'JUPITER'], ['SATURN', '568', '120,536', '687', '9.0', '35.5', '10.7', '10.7', '1432.0', '1357.6', '1506.5', '10,747', '9.7', '2.5', '0.052', '26.7', '-140', 'Unknown*', '83', 'Yes', 'Yes', 'SATURN'], ['URANUS', '86.8', '51,118', '1270', '8.7', '21.3', '-17.2', '17.2', '2867.0', '2732.7', '3001.4', '30,589', '6.8', '0.8', '0.047', '97.8', '-195', 'Unknown*', '27', 'Yes', 'Yes', 'URANUS'], ['NEPTUNE', '102', '49,528', '1638', '11.0', '23.5', '16.1', '16.1', '4515.0', '4471.1', '4558.9', '59,800', '5.4', '1.8', '0.010', '28.3', '-200', 'Unknown*', '14', 'Yes', 'Yes', 'NEPTUNE'], ['PLUTO', '0.0130', '2376', '1850', '0.7', '1.3', '-153.3', '153.3', '5906.4', '4436.8', '7375.9', '90,560', '4.7', '17.2', '0.244', '122.5', '-225', '0.00001', '5', 'No', 'Unknown', 'PLUTO']]


def planetData():
    data = None

    sys.path.insert(1, '../src/')
    from planets import Planet

    if TESTING:
        data = DATA
    else:
        URL = "https://nssdc.gsfc.nasa.gov/planetary/factsheet/"

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        table = soup.find('table')
        data = []

        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append(cols)

        data = transpose(data)

    planets = []

    for pRow in data[1:]:
        planet, mass, diameter, gravity = pRow[0], pRow[1], pRow[2], pRow[4]
        rotPeriod, oVelo, period, dist = pRow[6], pRow[12], pRow[11], pRow[8]
        if planet == 'MOON':
            continue
        planets.append(Planet(
            planet, mass, diameter, gravity, rotPeriod, oVelo, period, dist))

    return planets
