class Solution:
    def reverse(self, x: int) :
        a = x<0
        x = str(abs(x))
        length = len(x)
        c = ''
        for i in range(length):
            c = c + x[length-i-1]
        c = int(c)
        if a:
             c = -c
        if (c> -2**31 and c<2**31-1):
            return c
        else:
            return 0
