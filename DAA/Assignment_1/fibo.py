import time

# Iterative approach to calculate Fibonacci numbers
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Recursive approach to calculate Fibonacci numbers
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Function to calculate and display Fibonacci numbers up to n with complexities
def display_fibonacci_upto_n(n, method):
    print(f"\nCalculating Fibonacci numbers up to {n} using the {method} method.")
    
    if method == 'iterative':
        time_complexity = "O(n)"
        space_complexity = "O(1)"
        fib_function = fib_iterative
    elif method == 'recursive':
        time_complexity = "O(2^n)"
        space_complexity = "O(n)"
        fib_function = fib_recursive
    else:
        print("Invalid method selected.")
        return

    fibonacci_sequence = []
    start_time = time.time()

    for i in range(1, n + 1):
        fib_number = fib_function(i)
        fibonacci_sequence.append(str(fib_number))
    
    end_time = time.time()

    print(f"Fibonacci sequence up to {n}: {', '.join(fibonacci_sequence)}")
    print(f"Time taken = {end_time - start_time:.6f} seconds")
    print(f"Time Complexity: {time_complexity}")
    print(f"Space Complexity: {space_complexity}\n")

def menu():
    while True:
        print("\nChoose an option:")
        print("1. Calculate Fibonacci using Iterative method")
        print("2. Calculate Fibonacci using Recursive method")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1' or choice == '2':
            n = int(input("Enter the value of n: "))
            method = 'iterative' if choice == '1' else 'recursive'
            display_fibonacci_upto_n(n, method)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

menu()
