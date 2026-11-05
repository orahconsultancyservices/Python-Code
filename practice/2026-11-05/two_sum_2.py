"""
Problem: Two Sum
Given nums = [0, -12, 6, 2, 7, 8, 9, 5, 13, -3] and target = 14,
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
    nums = [0, -12, 6, 2, 7, 8, 9, 5, 13, -3]
    target = 14
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
