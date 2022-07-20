class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        split_list = []
        for i in range(len(sentences)):
            split_list.append(len(sentences[i].split(' ')))
        return max(split_list)