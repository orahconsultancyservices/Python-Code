"""
Problem: Two Sum
Given nums = [5, -11, 1, -19, 3, 13, 15, 8, 6] and target = 2,
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
    nums = [5, -11, 1, -19, 3, 13, 15, 8, 6]
    target = 2
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
