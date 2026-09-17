"""
Problem: Two Sum
Given nums = [-11, 18, 1, 7, 13, -9, -20, -19, -6, 2, 5] and target = 9,
return the indices of the two numbers that add up to target.
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


if __name__ == "__main__":
    nums = [-11, 18, 1, 7, 13, -9, -20, -19, -6, 2, 5]
    target = 9
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
