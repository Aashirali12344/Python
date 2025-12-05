def check_eligibility():

    
   
    
   
    age = int(input("Enter your age (18-30): "))
    percentage = float(input("Enter your academic percentage (>= 60): "))


    is_eligible = (18 <= age <= 30) and (percentage >= 60.0)
    
   
    print("\n--- Result ---")
    if is_eligible:
        print("✅ ELIGIBLE.")
    else:
        print("❌ NOT ELIGIBLE.")

if __name__ == "__main__":
    check_eligibility()