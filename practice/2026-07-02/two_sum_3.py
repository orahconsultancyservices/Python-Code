"""
Problem: Two Sum
Given nums = [-15, 10, 3, -10, -18, 13, 18, 8] and target = 16,
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
    nums = [-15, 10, 3, -10, -18, 13, 18, 8]
    target = 16
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
