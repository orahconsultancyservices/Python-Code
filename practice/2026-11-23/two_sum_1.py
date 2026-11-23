"""
Problem: Two Sum
Given nums = [-2, -10, 3, 17, 10, -13] and target = 13,
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
    nums = [-2, -10, 3, 17, 10, -13]
    target = 13
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
