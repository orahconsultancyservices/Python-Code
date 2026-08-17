"""
Problem: Two Sum
Given nums = [-15, -8, 9, -4, 8, 0, 16, -11, -1, 19] and target = -2,
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
    nums = [-15, -8, 9, -4, 8, 0, 16, -11, -1, 19]
    target = -2
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
