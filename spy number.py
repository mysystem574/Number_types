def is_spy_number(n):
    # Convert the number to a list of digits
    digits = [int(digit) for digit in str(n)]
    
    # Calculate the sum and product of the digits
    digit_sum = sum(digits)
    digit_product = 1
    for digit in digits:
        digit_product *= digit
    
    # Check if the sum is equal to the product
    return digit_sum == digit_product

# Test the function
number = int(input("Enter a number: "))
if is_spy_number(number):
    print(f"{number} is a spy number.")
else:
    print(f"{number} is not a spy number.")
