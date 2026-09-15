"""
Problem: Two Sum
Given nums = [-2, -7, 19, 1, 18, -17, 4] and target = 11,
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
    nums = [-2, -7, 19, 1, 18, -17, 4]
    target = 11
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
