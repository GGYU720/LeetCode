class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(int(len(nums) / 2)):
            result.append(nums[i])
            result.append(nums[i + n])
        return result