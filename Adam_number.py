def reverse_number(n):
    return int(str(n)[::-1])

def is_adam_number(n):
    # Reverse the number
    reversed_n = reverse_number(n)
    
    # Square both the original and reversed numbers
    n_squared = n ** 2
    reversed_n_squared = reversed_n ** 2
    
    # Check if the reverse of n_squared equals reversed_n_squared
    return reverse_number(n_squared) == reversed_n_squared

# Test the function
number = int(input("Enter a number: "))
if is_adam_number(number):
    print(f"{number} is an Adam number.")
else:
    print(f"{number} is not an Adam number.")
