dat=int(input("Enter the date "))
mon=int(input("Enter the month "))
if mon==1:
	rem=(31-dat)+(365-31)
elif mon==2:
	rem=(28-dat)+(365-59)
elif mon==3:
	rem=(31-dat)+(365-90)
elif mon==4:
	rem=(30-dat)+(365-120)
elif mon==5:
	rem=(31-dat)+(365-151)
elif mon==6:
	rem=(30-dat)+(365-181)
elif mon==7:
	rem=(31-dat)+(365-212)
elif mon==8:
	rem=(31-dat)+(365-243)
elif mon==9:
	rem=(30-dat)+(365-273)
elif mon==10:
	rem=(31-dat)+(365-304)
elif mon==11:
	rem=(30-dat)+(365-334)
elif mon==12:
	rem=(31-dat)
print("Remaining days are ",rem)
