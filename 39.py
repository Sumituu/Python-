#Calculate the volume of different 3D shapes (cube, sphere, cylinder).

import math

def calculate_volume_cube(side):
  

  volume = side ** 3
  return volume

def calculate_volume_sphere(radius):
  

  volume = (4 / 3) * math.pi * radius ** 3
  return volume

def calculate_volume_cylinder(radius, height):


  volume = math.pi * radius ** 2 * height
  return volume



cube_volume = calculate_volume_cube(10)
sphere_volume = calculate_volume_sphere(5)
cylinder_volume = calculate_volume_cylinder(3, 10)

print("The volume of the cube is:", cube_volume)
print("The volume of the sphere is:", sphere_volume)
print("The volume of the cylinder is:", cylinder_volume)
