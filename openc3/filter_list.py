import pytest

def test_filter_value_from_list():
    nums = [1, 2, 3, 2, 4, 5, 2, 1, 6]
    remove_it = 2
    result = list(filter(lambda x: x !=remove_it, nums))

    print (f"{result=}, {nums=}, len={len(result)}, removed number = {len(nums) - len(result)}")
    assert result == [1, 3, 4, 5, 1, 6]

def test_remove_elements_in_place():
    nums = [1, 2, 3, 2, 4, 5, 2, 1, 6]