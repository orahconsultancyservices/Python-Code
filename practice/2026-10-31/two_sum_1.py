"""
Problem: Two Sum
Given nums = [-11, 17, -16, 16, -14, 3, 19, 14] and target = 19,
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
    nums = [-11, 17, -16, 16, -14, 3, 19, 14]
    target = 19
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
