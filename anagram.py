n=input("Enter the First string ")
n1=input("Enter the Second string ")
a=sorted(n)
b=sorted(n1)
if a==b:
	print("The two strings are anagram.")
else:
	print("The two strings are not anagram.")
