def fibonacci(n):
    fib_numbers = [0, 1]  # Initial two numbers of Fibonacci sequence
    for i in range(2, n):
        next_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_number)
    return fib_numbers

# Input the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_numbers = fibonacci(n)
    print("Fibonacci numbers:")
    print(fibonacci_numbers)