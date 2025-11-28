name="Aashir"
age="13"
is_student=True
weight=40.8
print("Name",name)
print("the datatype of variable 'name' is ", type(name))
print("Age",age)
print("the datatype of variable 'age' is ", type(age))
print("is student",is_student)
print("the datatype of variable 'is student' is ", type(is_student))
print("weight",weight)
print("the datatype of variable 'weight' is ", type(weight))
print("after type casting")
age=str(age) 
print("Age",age)
print("the datatype of variable 'age' is ", type(age))
weight=int(weight) 
print("the datatype of variable 'weight' is ", type(weight))


num1=10
num2=30
print("number 1",num1)
print("number 2",num2)
print("Addition of number1 and number 2",num1+num2)
print("Subtraction of number1 and number 2",num1-num2)
print("Multiplication of number1 and number 2",num1*num2)
print("Division of number1 and number 2",num1/num2)
print(" Floor Division of number1 and number 2",num1//num2)
print("Modulus of number1 and number 2",num1%num2)
print("exponent of number1 and 2",num1**2)
print("Square root of number 1",num1**0.5)
print("if number1 and number2 are equal",num1==num2)
print("if number1 and number2 are not equal",num1!=num2)
print("if number 1 is greater than number 2",num1>num2)
print("if number 1 is less than number 2",num1<num2)
result= num1/2+num2**2+10
print("the result is ",result)

firstname="aashir"
lastname="ali"
fullname=firstname+lastname
print(fullname)
example= fullname*3
print(example)
word="codingisfun"
print("length of word is ",len(word))
print("first letter of string ",word[0])
print("lastletter of string ",word[-1])
print("slice of string ",word[3:7])

x=int(input("enter first number"))
y=int(input("enter second number"))
 temp=x
 x=y
 y=temp
 print("after swapping")
 print("X=",x)
 print("Y=",y)