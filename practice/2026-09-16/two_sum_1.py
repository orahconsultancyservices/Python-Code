"""
Problem: Two Sum
Given nums = [9, -3, -13, -11, 5, 1, 6, 12, 19] and target = 6,
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
    nums = [9, -3, -13, -11, 5, 1, 6, 12, 19]
    target = 6
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
