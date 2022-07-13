class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        while len(list_x) > 1:
            if list_x[0] == list_x[-1]:
                del(list_x[-1])
                if len(list_x) == 0:
                    return True
                del (list_x[0])
                if len(list_x) < 2:
                    return True
            else:
                return False
        return True