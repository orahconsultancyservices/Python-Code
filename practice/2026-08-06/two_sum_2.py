"""
Problem: Two Sum
Given nums = [-1, 0, 11, -14, 4, -8, -12, -9, -2, 12] and target = 23,
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
    nums = [-1, 0, 11, -14, 4, -8, -12, -9, -2, 12]
    target = 23
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
