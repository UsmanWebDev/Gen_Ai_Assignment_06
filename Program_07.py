def sum_of_numbers(numbers):
  
    total = 0   
    i = 0
 
    while i < len(numbers):
        total += numbers[i]
        i += 1

    return total


numbers = [1, 2, 3, 4, 5, 8, 9, 40, 45, 34]
print(sum_of_numbers(numbers))  