"""
Problem: Two Sum
Given nums = [8, 18, -10, -14, -17, 9, -13, -18, 16, 19, -9, 14] and target = 30,
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
    nums = [8, 18, -10, -14, -17, 9, -13, -18, 16, 19, -9, 14]
    target = 30
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
