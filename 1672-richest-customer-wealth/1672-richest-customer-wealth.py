class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sum_array = []
        for i in range(len(accounts)):
            sum_array.append(sum(accounts[i]))
        return max(sum_array)