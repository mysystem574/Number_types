import math

def is_strong_number(n):
    # Convert the number to a string to easily access its digits
    digits = str(n)
    
    # Calculate the sum of the factorials of the digits
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)
    
    # Check if the sum equals the original number
    return sum_of_factorials == n

# Test the function
number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong number.")
else:
    print(f"{number} is not a Strong number.")
