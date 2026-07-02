"""
Problem: Two Sum
Given nums = [16, 18, 5, 3, 8, 1, 11, -14, 0, 13] and target = 18,
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
    nums = [16, 18, 5, 3, 8, 1, 11, -14, 0, 13]
    target = 18
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
