class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        result = 0
        for i in range(len(operations)):
            if operations[i] in ["--X", "X--"]:
                result = result - 1
            else:
                result = result + 1
        return result