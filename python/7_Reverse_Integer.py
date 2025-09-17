class Solution(object):
    def reverse(self, x):
        INTEGER_MAX_INT = (2**31)-1
        INTEGER_MIN_INT = (-2**31)

        if x > INTEGER_MAX_INT or x < INTEGER_MIN_INT:
            return 0
        negative_num = x < 0
        revnum = 0
        x = abs(x)
        while x > 0:
            n = x %10
            x//=10
            if revnum > (INTEGER_MAX_INT - n)//10:
                return 0
            revnum = (revnum * 10) + n
        return -revnum if negative_num else revnum