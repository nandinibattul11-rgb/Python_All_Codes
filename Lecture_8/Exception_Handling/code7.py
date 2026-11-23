#One Block for Multiple Exceptions
try:
    num = int(input("Enter number: "))
    result = 100 / num
    print(result)
except (ValueError, ZeroDivisionError):
    print("Invalid operation.")