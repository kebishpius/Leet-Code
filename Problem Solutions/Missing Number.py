class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        if nums[-1] < len(nums):
            return nums[-1] + 1
        for i in range(0, len(nums)+1):
            if i != nums[i]:
                return i
