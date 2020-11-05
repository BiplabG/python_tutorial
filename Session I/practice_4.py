"""Write a python program with comments which takes radius and height of a cylinder as an input. 
Then it calculates total surface area and volume of cylinder and prints those values. 
TSA=πr^2 + 2πrh, Volume = πr^2h"""
import math

radius = float(input("Radius of the cylinder: \n"))
height = float(input("Height of the cylinder: \n"))

volume = math.pi * (radius ** 2) * height
tsa = math.pi * (radius**2) + (2*math.pi*radius*height)

print(f"Volume: {volume}. Total Surface Area: {tsa}")
