class Solution(object):
    def isPalindrome(self, x):
        # without using type conversion
        rev = 0
        temp = x
        while temp > 0:
            end_num = temp % 10
            rev = (rev * 10) + end_num
            temp = temp // 10
        return rev == x

        # using typeconversion
        return str(x) == str(x)[::-1]
