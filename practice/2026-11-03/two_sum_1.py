"""
Problem: Two Sum
Given nums = [-10, 5, -2, -11, 16, -7, -9, -13, -20, 19] and target = 35,
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
    nums = [-10, 5, -2, -11, 16, -7, -9, -13, -20, 19]
    target = 35
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
