                 #Program to find the type of Triangle
side1=eval(input("Enter Side1 "))
side2=eval(input("Enter Side2 "))
side3=eval(input("Enter Side3 "))
if (side1+side2)>side3 and (side3+side2)>side1 and (side1+side3)>side2:
	if (side1==side2) or (side2==side3) or (side1==side3):
		print("Isosceles Triangle")
	elif ((side1**2)+(side2**2)==side3**2) or ((side2**2)+(side3**2)==side1**2) or ((side3**2)+(side1**2)==side2**2):
		print("Right angle Triangle")
	else:
		print("Scalen Triangle")
else:
	print("Inavlid Sides")
