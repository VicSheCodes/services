
def shift_left(value: int, n: int) -> int:
    """
    Shifts the integer `value` to the left by `n` bits.
    Equivalent to multiplying `value` by 2**n.
    """
    return value << n

if __name__ == "__main__":
    n = 3  # Number of bits to shift
    original_value = 5  # Example value
    shifted_value = shift_left(original_value, n)
    print(f"Original value: {original_value}")
    print(f"Value after shifting left by {n} bits: {shifted_value}")