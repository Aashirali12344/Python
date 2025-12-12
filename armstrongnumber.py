def is_armstrong_number(number: int) -> bool:
    if number <= 0:
        return False

    number_str = str(number) 
    n = len(number_str) 
    
    original_number = number
    sum_of_powers = 0
    temp_number = original_number

    while temp_number > 0:
        digit = temp_number % 10
        sum_of_powers += digit ** n
        temp_number //= 10

    return sum_of_powers == original_number

while True:
    try:
        user_input = input("Enter a positive integer: ")
        
        if user_input.isdigit() and int(user_input) > 0:
            number_to_check = int(user_input)
            break
        else:
            print("Invalid input. Please enter a positive whole number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if is_armstrong_number(number_to_check):
    print(f"The number {number_to_check} IS an Armstrong number.")
else:
    print(f"The number {number_to_check} IS NOT an Armstrong number.")