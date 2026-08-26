"""
Problem: Two Sum
Given nums = [17, -2, 16, -3, -7, 0, 15, -13, -16, -11] and target = -18,
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
    nums = [17, -2, 16, -3, -7, 0, 15, -13, -16, -11]
    target = -18
    print("Input:", nums, "Target:", target)
    print("Result indices:", two_sum(nums, target))
