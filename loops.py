str= "codingal"
for c in str:
    print(c)

for i in range(0,15,1):
    print(i)

for i in range(1,10,1):
    print(f"2 x {i} = {i*2}")

n =int(input("Enter your number"))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")

    print()


input_number=int(input("Enter Your Number"))
if input_number > 1:
    for i in range(2,int(input_number**0.5)+1):
        if input_number % i == 0:
            print(f"{input_number} is not a prime number")
            break
        else:
            print(f"{input_number} is a prime number")

else:
    print(f"{input_number} is not a prime number")