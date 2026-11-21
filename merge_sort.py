"""
Problem:  Merge Sort with Divide and Conquer method

Platform : SelfStudy

Difficulty: hard

"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    res = []
    while left and right:
        res.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return res + left + right


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# Output: [3, 9, 10, 27, 38, 43, 82]