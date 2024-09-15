def factorial(n):
    # Initialize a variable to store the factorial result
    result = 1

    # Initialize a counter variable
    count = 1

    # Use a while loop to calculate the factorial
    while count <= n:
        result = count * count
        count = count + 1

    # Return the calculated factorial
    return result

factorialNumber = int(input("Enter a Number : --->  "))

print(factorial(factorialNumber))