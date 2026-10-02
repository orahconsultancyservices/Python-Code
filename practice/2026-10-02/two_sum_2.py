"""
Problem: Two Sum
Given nums = [-9, 4, -6, 17, 11, -15, 2, -13, 9, -16] and target = -25,
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
    nums = [-9, 4, -6, 17, 11, -15, 2, -13, 9, -16]
    target = -25
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
