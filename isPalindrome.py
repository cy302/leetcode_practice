class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        else:
            if (x % 10 == 0 and x != 0) or Solution().reverse(x) != x:
                return False
            else:
                return True

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0

        while x != 0:
            # pop the last digit in the current x to the back of the reverse number rev
            pop = x % 10
            x = x // 10

            if rev > sys.maxsize/10 or (rev == sys.maxsize/10 and pop > 7):
                return 0
            rev = rev * 10 + pop

        if rev > 2147483647:
            return 0

        return rev
