n=input("Enter the string ")
b=""
c=""
for i in range(0,len(n)):
	x=ord(n[i])
	if x>=65 and x<=90:
		b=b+n[i]
	else:
		c=c+n[i]
print(b)
print(c)
