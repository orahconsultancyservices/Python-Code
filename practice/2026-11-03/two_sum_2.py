"""
Problem: Two Sum
Given nums = [-12, 0, 9, 6, -13, -18, -17, -16] and target = -31,
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
    nums = [-12, 0, 9, 6, -13, -18, -17, -16]
    target = -31
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
