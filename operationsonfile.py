with open("sample.txt", "w") as f:
    f.write("Line 1: Python Basics\nLine 2: File Handling\nLine 3: OOP Concepts")

with open("sample.txt", "r") as f:
    content = f.read()
    print("--- Method 1: read() ---")
    print(content)

with open("sample.txt", "r") as f:
    print("\n--- Method 2: readline() ---")
    print(f.readline().strip())
    print(f.readline().strip())

with open("sample.txt", "r") as f:
    lines_list = f.readlines()
    print("\n--- Method 3: readlines() ---")
    print(lines_list)