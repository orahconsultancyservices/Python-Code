"""
Problem: Two Sum
Given nums = [-5, -20, 7, -2, 12, 9] and target = -8,
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
    nums = [-5, -20, 7, -2, 12, 9]
    target = -8
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
