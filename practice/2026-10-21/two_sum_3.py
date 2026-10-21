"""
Problem: Two Sum
Given nums = [18, 0, -17, -16, 15, 16, 17, 8] and target = 1,
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
    nums = [18, 0, -17, -16, 15, 16, 17, 8]
    target = 1
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
