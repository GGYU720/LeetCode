class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.append(sum(nums[0:i + 1]))
        return result