"""n = 3
fact = 1
i=1
while i<=n:
    fact*=i
    i+=1
print("Total fact = ",fact)"""

"""d=1
for i in range(1,6):
    for  j in range(1,i+1):
        print(d,end=" ")
        d+=1
    print()"""

"""n = int(input("Enter a number: "))
for i in range(10,0,-1):
    print(n*i)"""

"""name = input("Enter your name: ")
print('Good Morning ',name)"""

"""a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))

if a > b and a > c and a > d:
    print(a, "is greater")
elif b > a and b > c and b > d:
    print(b, "is greater")
elif c > a and c > b and c and d:
    print(c, " is greater")
else:
    print(d, " is greater")"""


"""list = ['Shrutika','Divya','Pallavi','Sakshi','Maliha','saloni']
x = 'Arya'
i = 0
for el in list:
    if el==x:
        print("Found at ",i)
    i+=1
else:
        print("Not Found")"""


"""ch = str(input("Enter username:"))

if (len(ch)<10):
    print(True)"""

"""marks = int(input("Enter marks: "))
if marks >=  90 and marks <= 100:
    print("Ex")
elif marks>= 80 and marks < 90:
    print("A")
elif marks >= 70 and marks < 80:
    print("B")
elif marks >=60 and marks < 70:
    print("C")
elif marks >= 50 and marks < 60:
    print("D")
else:
    print("F")"""


"""n = int(input("n="))
if n%2!=0:
    print(n,"is Prime")
else:
    print(n ,"is not Prime")"""

"""for i in range(1,21,2):
    print(i)"""

"""i=0
sum=0
while i<=15:
    sum+=i
    i+=1
print("sum=",sum)"""


"""sum = 0
for i in range(1,16):
    sum+=i
    i+=1
print("Total=",sum)"""

"""l = ["Harry", "Soham", "Sachin", "Rahul"]
print("Good Morning ",l[1])
print("Good Morning ",l[2])"""

"""for i in range(6,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()"""


"""Fruits = str(input("Enter Fruits: ")).split()
print("Fruits:",Fruits)"""

"""a = (7, 0, 8, 0, 0, 9)
print(a.count(0))"""

"""marks = [76,98,34,12,10,11,55,66]
print(marks.sort())
print(marks)"""

"""values = (input("values")).split(",")

list = values
print("List: ",list)
tuple = tuple(values)
print("tuple: ",tuple)"""

"""color_list = ["Red","Green","white","black"]
print(color_list[0])
print(color_list[-1])"""

"""l1 = [19,19,5,5,5,2]
if l1.count(19)==2 and l1.count(5)==3:
    print("True")
else:
    print("FALSE")"""

"""List = [9,3,2,5,5,5,7,8]
if len(List)==8 and List.count(List[4])==3:
    print("True")
else:
    print("False")"""

"""n = int(input("n="))
if n > 4**4 and n > 4%34:
    print("True")
else:
    print("False")"""

"""lst = list(range(10))
print(lst)"""

"""for i in range(1,7):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()"""

"""for i in range(1,7):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()"""

import pdfkit

# URL of the CodeWithHarry Python tutorial
url = 'https://www.codewithharry.com/tutorial/overview/python'

# Output PDF file path
output_pdf = 'CodeWithHarry_Python_Tutorial.pdf'

# Convert the webpage to PDF
pdfkit.from_url(url, output_pdf)

print(f"PDF saved as {output_pdf}")























































