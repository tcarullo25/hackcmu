import sys
import requests
from bs4 import BeautifulSoup


def transpose(matrix):
    result = []
    rows, cols = len(matrix), len(matrix[0])
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result


def planetData():
    sys.path.insert(1, '../src/')
    from planets import Planet

    URL = "https://nssdc.gsfc.nasa.gov/planetary/factsheet/"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find('table')
    data = []

    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)  # Get rid of empty values

    data = transpose(data)
    planets = dict()

    for pRow in data[1:]:
        planet, mass, diameter = pRow[0], pRow[1], pRow[2]
        gravity, rotPeriod, v, period = pRow[4], pRow[6], pRow[11], pRow[10]
        planets[planet] = Planet(
            planet, mass, diameter, gravity, rotPeriod, v, period)

    return planets
