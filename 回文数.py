class Solution:
    def isPalindrome(self, x: int):
        x = str(x)
        l = len(x)
        for i in range(l):
            if i > l / 2 - 1:
                break
            if x[i] != x[l - i - 1]:
                return False
        return True
