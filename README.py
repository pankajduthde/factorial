# Factorial-function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120

import math

# Step 1: Ask the user for a number
num = float(input("Enter a number: "))

# Step 2: Perform calculations using the math module
# Note: log and sqrt are only valid for positive numbers
if num > 0:
    square_root = math.sqrt(num)
    natural_log = math.log(num)
else:
    square_root = "Undefined (must be >= 0)"
    natural_log = "Undefined (must be > 0)"

sine_value = math.sin(num)  # Works for all real numbers (radians)

# Step 3: Display the results
print("\n--- Results ---")
print(f"Square root of {num}       : {square_root}")
print(f"Natural logarithm of {num} : {natural_log}")
print(f"Sine of {num} radians       : {sine_value}")
