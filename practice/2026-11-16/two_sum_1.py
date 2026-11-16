"""
Problem: Two Sum
Given nums = [-18, 12, 4, -19, 19, -5, 2, 13, 10, 0, -12, 18] and target = 20,
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
    nums = [-18, 12, 4, -19, 19, -5, 2, 13, 10, 0, -12, 18]
    target = 20
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
