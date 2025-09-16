def twoSum(self, nums, target):
    d = {}
    for i, num in enumerate(nums):
        compliment = target - nums[i]
        if compliment in d:
            return [d[compliment], i]
        d[num] = i