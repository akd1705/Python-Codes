                #Program to calculate Simple Interest
princ=eval(input("Enter the Principal amount "))
rate=eval(input("Enter the Rate of Interest "))
time=eval(input("Enter the Time "))
si=((princ*rate*time)/100)
amount=princ+si
print("Simple Interest= ",si,"Amount= ",amount)
