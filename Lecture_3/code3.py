s = input("Enter a sentence: ")
w = s.split()
print("The words in the list are:", w)
l = ""
for i in w:
    if len(i) > len(l):
        l = i
print("The longest word in the sentence is:", l)
