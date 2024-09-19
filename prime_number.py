def is_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return False
    # Check if n has any divisors other than 1 and itself
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
