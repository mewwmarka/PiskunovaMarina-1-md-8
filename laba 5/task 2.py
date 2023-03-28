numbers = [1, 6, 3, 6, 5, 7, 8, 10]
povtor = {i for i in numbers if numbers.count(i) > 1}
print(povtor)