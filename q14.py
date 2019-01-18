               #Program To calculate Compound Interest
princ=eval(input("Enter the principal amount "))
time=eval(input("Enter the time in years "))
rate=eval(input("Enter the rate "))
nn=eval(input("Enter the time to be compounded anually "))
amount=(princ*((1+(rate/nn)))**(time*nn))
comp=amount-princ
print("Compound Interest=",comp,"Amount=",amount)
