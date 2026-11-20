"""
Problem:  N-Queens Problem solve using Backtracking

Platform : SelfStudy

Difficulty: hard
"""

def get_subsets(nums):
    result = []
    current = []

    def backtrack(index):
        # Base case: reached the end of the list
        if index == len(nums):
            result.append(current[:])
            return

        # 1. CHOOSE: Include nums[index]
        current.append(nums[index])
        # 2. EXPLORE: Move to the next number
        backtrack(index + 1)

        # 3. UNCHOOSE (Backtrack): Remove nums[index]
        current.pop()
        # Explore the path without nums[index]
        backtrack(index + 1)

    backtrack(0)
    return result


print(get_subsets([1, 2]))
# Output: [[1, 2], [1], [2], []]