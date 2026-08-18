"""
Problem: Two Sum
Given nums = [8, 15, -8, -6, 13, 3, 6, 0, -20, -15, -2] and target = -17,
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
    nums = [8, 15, -8, -6, 13, 3, 6, 0, -20, -15, -2]
    target = -17
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
