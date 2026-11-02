"""
Problem: Two Sum
Given nums = [0, 4, 14, -14, -10, 13, 15, -5, -16, -1] and target = 10,
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
    nums = [0, 4, 14, -14, -10, 13, 15, -5, -16, -1]
    target = 10
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
