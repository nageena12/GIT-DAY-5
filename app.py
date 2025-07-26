# Sample Python code to check if numbers are even or odd

def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is even")

# List of numbers
num_list = [1, 2, 3, 25, 5, 6, 7, 8, 9, 10]

# Calling the function
check_even_odd(num_list)
