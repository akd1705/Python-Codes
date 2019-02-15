n=input("Enter the string ")
rev=""
for i in range(0,len(n)):
	rev=n[i]+rev
if n==rev:
	print("The String is Palindrome.")
else:
	print("The string is not Palindrome.")
