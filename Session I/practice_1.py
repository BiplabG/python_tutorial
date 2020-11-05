"""Write a program, which prompts user perpendicular and base of a right angle triangle and returns the hypotenuse back to the user."""
import math
perpendicular = float(input("Enter the perpendicular:\n"))
base = float(input("Enter the base: \n"))

hypotenuse = math.sqrt(perpendicular**2 + base**2)
print(f"Hypotenuse: {hypotenuse}")
