#Print the Following Pattern
n = int(input("n = "))
for i in range(1,n+1):
    print(" " * (n-i),end = "")
    for j in range(1,i+1):
        if i%2!=0:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()