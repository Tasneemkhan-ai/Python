#Aim:TO cheeck whether prime or not
#Name:Khan Tasneem
#Date:15-04-2026
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if number == 2:
        return True   # 2 is the only even prime number
    if number % 2 == 0:
        return False  # Other even numbers are not prime

    # Check for divisors from 3 up to the square root of the number, skipping even numbers
    limit = int(math.sqrt(number)) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False

    return True

num = int(input("Enter a number to check: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
