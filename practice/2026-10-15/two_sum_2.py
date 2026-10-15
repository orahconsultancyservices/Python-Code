"""
Problem: Two Sum
Given nums = [2, 4, -1, -7, 17, -13, 6] and target = 23,
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
    nums = [2, 4, -1, -7, 17, -13, 6]
    target = 23
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
