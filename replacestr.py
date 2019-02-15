n=input("Enter the string ")
c=""
for i in range(0,len(n)):
	x=ord(n[i])
	if x%2==0:
		c=c+"#"
	else:
		c=c+n[i]
print(c)
