import os
import sys
from easytello import tello

my_drone = tello.Tello()
my_drone.streamon()
my_drone.takeoff()



def searchforinput():
    key = input()
    if key == "w":
        my_drone.forward(20)
    if key == "s":
        my_drone.back(20)
    if key == "a":
        my_drone.left(20)
    if key == "d":
        my_drone.right(20)
    if key == "h":
        my_drone.land()
    if key == "1":
        my_drone.up(20)
    if key == "2":
        my_drone.down(20)
    if key == "3":
        my_drone.flip("b")
    if key == "close":
        exit()
    searchforinput()

searchforinput()

"""address = "192.168.10.1"
port = 8889"""