class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = sorted([i for i in str(num)])
        return int(''.join([num_list[0], num_list[2]])) + int(''.join([num_list[1], num_list[3]]))