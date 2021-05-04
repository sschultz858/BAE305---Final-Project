"""
Consume LIDAR measurement file and create an image for display.

Adafruit invests time and resources providing this open source code.
Please support Adafruit and open source hardware by purchasing
products from Adafruit!

Written by Dave Astels for Adafruit Industries
Copyright (c) 2019 Adafruit Industries
Licensed under the MIT license.

All text above must be included in any redistribution.
"""

import os
from math import cos, sin, pi, floor, sqrt, pow
import pygame
from adafruit_rplidar import RPLidar
from itertools import chain

# Set up pygame and the display
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((320,240))
pygame.mouse.set_visible(False)
lcd.fill((0,0,0))
pygame.display.update()

# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME)

# used to scale data to fit on the screen
max_distance = 0
stopped = False


danger_distance = 1500
#pylint: disable=redefined-outer-name,global-statement
def process_data(data):     #def starts a function, process_data is the name
    global max_distance
    global stopped
    lcd.fill((0,0,0))
    danger_flag = False
    for angle in chain(range(350,360), range(0,10)):
        distance = data[angle]
        if distance > 0:     # ignore initially ungathered data points
            max_distance = max([min([5000, distance]), max_distance])
            radians = angle * pi / 180.0
            x = distance * cos(radians)
            y = distance * sin(radians)
            point = (160 + int(x / max_distance * 119), 120 + int(y / max_distance * 119))
            lcd.set_at(point, pygame.Color(255, 255, 255))
            print(f"angle:{angle},\tdistance:{distance}")
            if distance < danger_distance:
                danger_flag = True
    if danger_flag:
        print("stop")
        stopped = True
    else:
        print("clear")
        stopped = False

#                 if stopped == True:
#                     print("Just Cleared")
#                     stopped = False

    
    pygame.display.update()



scan_data = [0]*360

try:
#     if actual_distance > 10:
    print(lidar.info)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
        process_data(scan_data)
    
  #  if actual_distance < 10:
       # print("STOP")
       # lidar.stop()
    
except KeyboardInterrupt:
    print('Stoping.')
lidar.stop()
lidar.disconnect()
