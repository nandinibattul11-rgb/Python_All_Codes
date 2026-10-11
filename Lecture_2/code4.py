#Accept name and check wheteher it is plaindrome or not
s = str(input("Enter the Name: "))
s = s.strip()
if s == s[::-1]:
    print(s,"is palindrome")
else:
    print(s,"is not palindrome")
    