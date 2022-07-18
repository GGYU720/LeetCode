class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        result = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if (strs[0][i] == strs[j][i]):
                    if j == len(strs) - 1:
                        result += strs[0][i]
                else:
                    return result
        return result