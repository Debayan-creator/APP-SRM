def sum(x, y):
    sum = x + y
    if sum in range(105, 200):
        return 200
    else:
        return sum
print(sum(100, 8))
print(sum(100, 2))
print(sum(100, 36))