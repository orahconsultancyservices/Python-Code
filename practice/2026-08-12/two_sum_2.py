"""
Problem: Two Sum
Given nums = [-3, -19, 19, 2, -18, 3, -13, 6, -1] and target = -20,
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
    nums = [-3, -19, 19, 2, -18, 3, -13, 6, -1]
    target = -20
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
