"""
Problem: Two Sum
Given nums = [17, 11, 4, 3, 2, 9, -9, 6, -5, 19] and target = 0,
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
    nums = [17, 11, 4, 3, 2, 9, -9, 6, -5, 19]
    target = 0
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
