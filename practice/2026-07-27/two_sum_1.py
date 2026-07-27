"""
Problem: Two Sum
Given nums = [19, 7, -19, 0, -13, -18, -14, -9, -3, -7] and target = -25,
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
    nums = [19, 7, -19, 0, -13, -18, -14, -9, -3, -7]
    target = -25
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
