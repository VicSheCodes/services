
#
# arr1 = [(6, 8), (1, 3), (5, 7), (2, 11)]

# arr1 = [(2, 6), (3, 7), (3, 5)]

arr1 = [(2, 3)]


def merge_intervals(arr):
    if not arr:
        return []

    # Sort intervals based on the starting time
    arr.sort(key=lambda x: x[0])
    merged = [arr[0]]

    for current in arr[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:  # There is an overlap
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))  # Merge
        else:
            merged.append(current)

    return merged



# if __name__ == "__main__":
def test_merge_intervals():
     print(merge_intervals(arr1))

     assert merge_intervals([]) == []
     # 1. Empty Input Should return: []

     assert merge_intervals([(1, 3)]) == [(1, 3)]
     #  Single Interval Should return: [(1, 3)]

     assert merge_intervals([(1, 2), (3, 4), (5, 6)]) == [(1, 2), (3, 4), (5, 6)]
     #  No Overlaps Should return: [(1, 2), (3, 4), (5, 6)]

     assert merge_intervals([(1, 4), (2, 5), (3, 6)]) == [(1, 6)]
     # All Intervals Overlap Should return: [(1, 6)]

     assert merge_intervals([(1, 3), (3, 5)]) == [(1, 5)]
     # Adjacent Intervals (Touching) Should return: [(1, 5)] - since 3 <= 3 is true

     assert merge_intervals([(2, 5), (2, 5), (2, 5)]) == [(2, 5)]
     #  Identical Intervals Should return: [(2, 5)]

     assert merge_intervals([(2, 2), (2, 3), (3, 3)]) ==  [(2, 3)]
     #  Point Intervals (Start = End) Should return: [(2, 3)]

     assert merge_intervals([(1, 10), (2, 3), (4, 5)]) == [(1, 10)]
     #  Nested Intervals Should return: [(1, 10)]

     assert merge_intervals([(6, 8), (1, 3), (2, 4)]) == [(1, 4), (6, 8)]
     # Should handle sorting automatically

