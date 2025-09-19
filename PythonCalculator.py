# ─────────────────────────────
# Simple Python Calculator
# Author: Rezvan, Bahara Rahmati
# Description: A user-friendly calculator that supports
# addition, subtraction, multiplication, division, and exponentiation.
# ─────────────────────────────

print("\n\nˏˋ°•*⁀➷")
print("─────────ೆೊೋღ Welcome to My Calculator! ღೋೊೆ─────────\n")

# Get user inputs
num1 = float(input("Enter the first number: "))
operation = input("Choose the operation (+, -, /, *, ^): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on the chosen operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result:.2f}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result:.2f}")

elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result:.2f}")

elif operation == "^":
    result = num1 ** num2
    print(f"{num1}^{num2} = {result:.2f}")

else:
    print("Invalid operator! Please use one of (+, -, /, *, ^).")
