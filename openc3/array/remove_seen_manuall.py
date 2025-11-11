
""""
Remove Duplicates from a List (In-Place)
    Create an empty set to track seen elements.
    Iterate through the list using an index.
    If the current element is in the set, remove it from the list.
    Otherwise, add it to the set and move to the next index.
"""
def remove_seen_numbers():
    numbers = [1, 1, 2, 3, 3, 4, 5, 5, 6]
    seen = set()

    for num in numbers:
        if num not in seen:
            seen.add(num)
        else:
            numbers.pop(numbers.index(num))

    print(f"Unique numbers: {seen}, final array: {numbers=}")


"""
Remove Duplicated Characters from a String (In-Place)
    Convert the string to a list of characters (since strings are immutable in Python).
    Create an empty set to track seen characters.
    Iterate through the list of characters using an index.
    If the character is in the set, remove it from the list.
    Otherwise, add it to the set and move to the next index.
    Convert the list back to a string.
"""


"""
remove duplicates from a string without converting it to a list 
by using a set to track seen characters and building a new string 
as you iterate through the original string. 
"""

def remove_duplicates_from_string():
    original_string = "hello world"
    seen = set()
    result = []

    for char in original_string:
        if char not in seen:
            seen.add(char)
            result.append(char)

    final_string = ''.join(result)
    print(f"Original string: {original_string}, Unique characters: {seen}, Final string: {final_string}")

if __name__ == "__main__":
    remove_seen_numbers()