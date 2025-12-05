def swap_three_numbers():


    try:
        a = float(input("Enter first number (A): "))
        b = float(input("Enter second number (B): "))
        c = float(input("Enter third number (C): "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    print(f"\nBefore Swap: A={a}, B={b}, C={c}")
    
   
    a, b, c = b, c, a
    
    print(f"After Swap:  A={a}, B={b}, C={c}")

if __name__ == "__main__":
    swap_three_numbers()