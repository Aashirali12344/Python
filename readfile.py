with open("data.txt", "w") as f:
    f.write("Line 1: Python\nLine 2: Java\nLine 3: C++")

with open("data.txt", "r") as f:
    print(f.read())

with open("data.txt", "r") as f:
    f.seek(0)
    print(f.readline())

with open("data.txt", "r") as f:
    f.seek(0)
    print(f.readlines())