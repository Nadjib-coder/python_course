try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", result)
finally:
    print("Exception handling completed.")
