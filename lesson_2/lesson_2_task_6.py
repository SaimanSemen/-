lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
result = list(filter(lambda x: x < 30 and x % 3 == 0, lst))
print(result)