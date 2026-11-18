#Functional Programming filter()
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

nums = [20, 55, 80, 25, 60,54,89]
result = list(filter(lambda x: x > 50, nums))
print(result)
