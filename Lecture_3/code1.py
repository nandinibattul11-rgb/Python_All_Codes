#1.	Write a program to read a file and count how many vowels are present in its content.

f = open("Lecture_3/sample.txt")
content = f.read()

count = 0
vowels = 'aeiouAEIOU'
for i in content:
    if i in vowels:
        count = count + 1
print(content)
print("Total Vowels:",count)
f.close()