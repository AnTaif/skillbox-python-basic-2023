import math

def calculate_square_root(number):
    try:
        result = math.sqrt(number)
        return result
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"Unexpected error: {e}"

try:
    input_number = float(input("Enter a number to calculate its square root: "))
    result = calculate_square_root(input_number)
    print(f"The square root of {input_number} is: {result}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")
