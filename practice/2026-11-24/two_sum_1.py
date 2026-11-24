"""
Problem: Two Sum
Given nums = [1, -17, -3, -11, 8, -1, -9, -19, 19, -16, 2, 5] and target = 3,
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
    nums = [1, -17, -3, -11, 8, -1, -9, -19, 19, -16, 2, 5]
    target = 3
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
