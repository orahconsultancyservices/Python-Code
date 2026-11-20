"""
Problem: Two Sum
Given nums = [14, 6, -13, 3, 7, 18, -15, -20, -14, -7] and target = 3,
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
    nums = [14, 6, -13, 3, 7, 18, -15, -20, -14, -7]
    target = 3
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
