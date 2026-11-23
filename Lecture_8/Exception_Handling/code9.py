#Using Finally Block
try:
    file = open("test.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program completed.")