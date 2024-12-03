from graphics import circle,rectangle
r=int(input("Enter the radius of circle:"))
circle.areac(r)
circle.perimc(r)

l=int(input("\nEnter the length of rectangle:"))
b=int(input("\nEnter the breadth of rectangle:"))
rectangle.arear(l,b)
rectangle.perimr(l,b)

from graphics.dgraphics import cuboid,sphere
l1=int(input("\nEnter the length of cuboid:"))
b1=int(input("\nEnter the breadth of cuboid:"))
h1=int(input("\nEnter the height of cuboid:"))
cuboid.areacub(l1,b1,h1)
cuboid.perimcub(l1,b1,h1)

r1=int(input("Enter the radius of sphere:"))
sphere.areas(r1)
sphere.perims(r1)
