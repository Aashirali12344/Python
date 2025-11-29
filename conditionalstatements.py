num=int(input("Enter Your Number"))
print("You have entered",num)
if num%2 == 0:
    print("The number is even")
else:
    print("The number is odd")


height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))
BMI=weight/(height/100)**2
print("your body mass index is: ",BMI)

if BMI>0:
    if BMI<=16:
        print("you are severly underweight")
if BMI<=18.5:
    print("you are underweight")
if BMI<=25:
    print("you are healthy")
elif BMI<=30:
    print("you are overweight")
else:
    print("you are severely overweight")


number=int(input("enter your number"))
if num >=50:
    print("number is greater than 50")
    if (num%2==0):
        print("the number is even too")
    else:
        print("this is odd number")
else:
    print("number is less than 50")


from IPython.core.history import datetime
current_time=datetime.datetime.now()
print("time is ",current_time)
import calender
print("\n",calender.calender(2025))