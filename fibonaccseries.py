def generate_fibonacci(n_terms):
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    
    fib_series = [0, 1] 
    
    for i in range(2, n_terms):
        next_term = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_term)
    
    return fib_series

def main():
    print("✨ Fibonacci Series Generator ✨")
    
    while True:
        try:
            user_input = input("Enter the number of terms (n) for the series: ")
            n = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    series = generate_fibonacci(n)
    
    print(f"\nResults for N = {n} terms:")
    if n <= 0:
        print("The number of terms must be a positive integer.")
    else:
        print(series)
        print(f"\nThe Fibonacci series has {len(series)} terms.")

if __name__ == "__main__":
    main()