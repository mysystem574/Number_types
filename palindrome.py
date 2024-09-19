def is_palindrome(n):
    # Convert the number to a string
    str_n = str(n)
    
    # Check if the string is the same when reversed
    return str_n == str_n[::-1]

# Test the function
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
