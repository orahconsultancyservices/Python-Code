"""
Problem: Two Sum
Given nums = [10, -12, 15, 19, 12, -2, -14, 11] and target = 8,
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
    nums = [10, -12, 15, 19, 12, -2, -14, 11]
    target = 8
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
