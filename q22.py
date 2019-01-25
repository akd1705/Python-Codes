x=int(input("Enter the x coordinate of Center of Circle "))
y=int(input("Enter the y coordinate of Center of Circle "))
radius=int(input("Enter the radius of Circle "))
x1=int(input("Enter the x coordinate of the point "))
y1=int(input("Enter the y coordinate of the point "))
distance=(((x-x1)**2)+((y-y1)**2))**0.5
if distance<radius:
	print("The point is inside the Circle.")
elif distance>radius:
	print("The point is outside the Circle.")
else:
	print("The point is on the Circle.")
