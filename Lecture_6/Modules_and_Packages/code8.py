#Functional Programming Map
nums = [1,3,5,7]
result = list(map(lambda x: x*2, nums))
print(result)

names = ["Pallavi","Shrutika","Divya"]

result = list(map(str.upper, names))
print(result)
