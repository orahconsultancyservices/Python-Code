"""
Problem: Two Sum
Given nums = [18, 1, 12, 13, -13, -17, -20, -19, -2, -15, 2, 6] and target = 4,
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
    nums = [18, 1, 12, 13, -13, -17, -20, -19, -2, -15, 2, 6]
    target = 4
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
