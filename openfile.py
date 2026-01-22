with open("activity.txt", "w") as f:
    f.write("Mode: Write\n")
    f.write("This overwrites the file.\n")

with open("activity.txt", "a") as f:
    f.write("Mode: Append\n")
    f.write("This adds to the end.\n")

with open("activity.txt", "r") as f:
    print(f.read())

with open("activity.txt", "r+") as f:
    f.write("New Start")

with open("activity.txt", "w+") as f:
    f.write("New file with read/write")
    f.seek(0)
    print(f.read())