
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]


i = 0
while i < len(numbers):
    if numbers[i] < 0:
        numbers.pop(i)
    else:
        i += 1


print(numbers)