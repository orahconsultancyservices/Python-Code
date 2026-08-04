"""
Problem: Two Sum
Given nums = [-2, -11, 15, 9, -19, 17, 11, -14, -7] and target = 24,
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
    nums = [-2, -11, 15, 9, -19, 17, 11, -14, -7]
    target = 24
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
