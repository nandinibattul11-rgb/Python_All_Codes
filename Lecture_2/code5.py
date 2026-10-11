#print the sum of digits
num = int(input("Enter a number: "))
total = 0

for digit in str(abs(num)):
    total += int(digit)

if num < 0:
    total = -total

print("Sum of digits:", total)