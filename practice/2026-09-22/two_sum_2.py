"""
Problem: Two Sum
Given nums = [-6, 18, 1, -1, 0, -12, -14, -19, 17] and target = -7,
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
    nums = [-6, 18, 1, -1, 0, -12, -14, -19, 17]
    target = -7
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
