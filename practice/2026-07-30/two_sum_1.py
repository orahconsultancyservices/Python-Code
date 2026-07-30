"""
Problem: Two Sum
Given nums = [15, -14, 18, 11, 19, 0, 2, -7, -13, -20, 9, 6] and target = 34,
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
    nums = [15, -14, 18, 11, 19, 0, 2, -7, -13, -20, 9, 6]
    target = 34
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
