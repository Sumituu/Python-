# Calculate the area of a circle segment.

import math

def area_of_circle_segment(radius, central_angle):
    return 0.5 * radius**2 * (central_angle - math.sin(central_angle))

radius = 5.0  
central_angle = math.radians(60) 

area = area_of_circle_segment(radius, central_angle)
print(f"The area of the circle segment is {area:.2f} square units.")
