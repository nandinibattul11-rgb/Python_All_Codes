#2.	Read all lines from a file into a list. Print the total number 
# of lines and display the 2nd and 4th line.
f = open("Lecture_3/sample.txt")
line = f.readlines()

print(len(line))
print(line[1])
print(line[3])
f.close()