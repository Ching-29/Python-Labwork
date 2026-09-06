# Program to calculate factorial and check prime number

# Factorial Calculation
num = int(input("Enter a number to calculate factorial: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print("Factorial =", 1)
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial =", factorial)

# Prime Number Check
n = int(input("\nEnter a number to check if it is prime: "))

if n <= 1:
    print(n, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
