"""
Problem: Two Sum
Given nums = [-13, 12, 8, -15, -2, -6, -12, 7, 15, 9] and target = 9,
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
    nums = [-13, 12, 8, -15, -2, -6, -12, 7, 15, 9]
    target = 9
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
