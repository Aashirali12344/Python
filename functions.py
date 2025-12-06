def sample_function():
    print("this is sample function")

sample_function()

def second_function():
    sum=2+3
    return sum

additon = second_function()
print("the sum is", additon)
print(second_function())

def intro(name):
    print(" Hello! Good Morning I am ",name)


user_input=input("Enter your name: ")
intro(user_input)


def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
    
n= int(input("Enter the Number:"))
if n<0:
    print("Factorial cannot be calculated for negative numbers")
elif  n==0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of",n,"is",recur_factorial(n))



def add(x,y):
    return (x+y)

def subtract(x,y):
    return (x-y)

def mul(x,y):
    return(x*y)

def div(x,y):
    return(x/y)

num1=int(input("Enter first Number :"))
num2=int(input("Enter Second number :"))
print("the sum is ",add(num1,num2))
print("the difference is ",subtract(num1,num2))
print("the product is ",mul(num1,num2))
print("the division is ",div(num1,num2))