"""
Problem: Two Sum
Given nums = [-5, 3, -8, 10, -14, -2, 0, 18, 13, -7] and target = 16,
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
    nums = [-5, 3, -8, 10, -14, -2, 0, 18, 13, -7]
    target = 16
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
