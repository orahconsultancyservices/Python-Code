"""
Problem: Two Sum
Given nums = [11, -7, -18, -2, 6, -1, 4, 13, 7, -3, -11] and target = -5,
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
    nums = [11, -7, -18, -2, 6, -1, 4, 13, 7, -3, -11]
    target = -5
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
