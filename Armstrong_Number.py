def is_armstrong_number(n):
    # Convert the number to a string to easily access its digits
    digits = str(n)
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum equals the original number
    return sum_of_powers == n

# Test the function
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
