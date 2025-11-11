"""
Number Generator (Generators + Exceptions)
Create a generator that yields even numbers but stops on invalid input.

"""

def safe_even_numbers(max_num):
    """
    Generate even numbers from 0 to max_num.
    Raise ValueError if max_num is negative.
    Raise TypeError if max_num is not an integer.
    """

    if not isinstance(max_num, int):
        raise TypeError("max_num must be an integer\n")
    if max_num < 0:
        raise ValueError("max_num cannot be negative\n")

    try:
        start = 0
        while start <= max_num:
            yield start
            start += 2

    finally:
        print("Generator cleanup in safe_even_numbers.") # Runs when generator closes/exhausts


if __name__ == '__main__':
    print("=== Test 1: Normal case ===")
    for num in safe_even_numbers(10):
        print(num)  # 0, 2, 4, 6, 8, 10

    print("\n=== Test 2: Negative number (should raise ValueError) ===")
    try:
        for num in safe_even_numbers(-5):
            print(num)
    except ValueError as e:
        print(f"✅ Caught ValueError: {e}")

    print("\n=== Test 3: String input (should raise TypeError) ===")
    try:
        for num in safe_even_numbers("10"):
            print(num)
    except TypeError as e:
        print(f"✅ Caught TypeError: {e}")

    print("\n=== Test 4: Edge case (max_num = 0) ===")
    for num in safe_even_numbers(0):
        print(num)  # Should print just 0

    print("\n=== Test 5: Edge case (max_num = 1) ===")
    for num in safe_even_numbers(1):
        print(num)  # Should print just 0