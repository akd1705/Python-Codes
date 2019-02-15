n=input("Enter the first string ")
n1=input("Enter the second string ")
if n in n1:
	print(n,"is substring of",n1)
elif n1 in n:
	print(n1,"is substring of",n)
else:
	print("No two strings are substring of eachother.")
