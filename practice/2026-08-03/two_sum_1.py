"""
Problem: Two Sum
Given nums = [-12, 3, 11, -20, 6, -7, -19, -13, -17, -11, 5, -9] and target = -13,
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
    nums = [-12, 3, 11, -20, 6, -7, -19, -13, -17, -11, 5, -9]
    target = -13
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
