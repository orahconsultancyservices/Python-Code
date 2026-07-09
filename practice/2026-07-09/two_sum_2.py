"""
Problem: Two Sum
Given nums = [-19, 10, -18, -20, 16, -11] and target = -9,
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
    nums = [-19, 10, -18, -20, 16, -11]
    target = -9
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
