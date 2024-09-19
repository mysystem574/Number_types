def sum_of_digits(n):
    # Calculate the sum of the digits of a number
    return sum(int(digit) for digit in str(n))

def is_magic_number(n):
    # Repeatedly sum digits until a single digit is obtained
    while n > 9:
        n = sum_of_digits(n)
    
    # Check if the single digit is 1
    return n == 1

# Test the function
number = int(input("Enter a number: "))
if is_magic_number(number):
    print(f"{number} is a magic number.")
else:
    print(f"{number} is not a magic number.")
