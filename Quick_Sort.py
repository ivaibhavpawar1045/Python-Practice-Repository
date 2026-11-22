"""
Problem:  Profram which solves Quick Sort

Platform : SelfStudy

Difficulty: hard

"""


def quick_sort(arr):
    # Base case: 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Pick the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([38, 27, 43, 3, 9, 82, 10]))
# Output: [3, 9, 10, 27, 38, 43, 82]