# HackCMU 2023: Space Navigate

## Overview

Space Navigate is an application that lets you navigate through the solar system taking into account realistic planetary factors such as mass, diameter, density, gravity, orbital speed, and more. This project combines Python for data scraping along with MATLAB for complex calculations related to orbital dynamics.

### Features

- **Real-time Data**: The application scrapes real-time planetary data (though a testing mode with static data is also available).
- **Planetary Movement**: Planets move in their orbits in real-time based on their actual orbital periods and speeds.
- **Realistic Calculations**: Uses MATLAB to run simulations and calculate the optimal paths for space travel between planets.

## Code Structure

### Python

- `transpose(matrix)`: Transposes a given matrix.
- `planetData()`: Fetches or uses static planetary data to create a list of Planet objects.
- `distance(x0, y0, x1, y1)`: Calculates the Euclidean distance between two points.
- `polarToRectangular(app, distance, theta)`: Converts polar coordinates to rectangular coordinates.
- `run_matlab_script(...)`: Executes a MATLAB script and reads its output.
- `Planet`: Class that holds attributes and methods related to a planet.

### MATLAB

- `traj(...)`: Function to calculate the trajectory between two points in a 2D plane.
- `calculate_trajectory.m`: Main script that reads inputs, runs the trajectory calculations, and verifies the results.

## Requirements

- Python 3.x
- MATLAB
- Requests library for Python
- BeautifulSoup for Python

## Authors

- [Tim Carullo](mailto:tcarullo@andrew.cmu.edu)
- [Sam Chen](mailto:samuelch@andrew.cmu.edu)
- [Ethan Kwong](mailto:jieunlim@andrew.cmu.edu)
- [Jieun Lim](mailto:ethankwo@andrew.cmu.edu)
