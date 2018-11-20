class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        ind = True

        if x < 0:
            x = -x
            ind = False

        while x != 0:
            # pop the last digit in the current x to the back of the reverse number rev
            pop = x % 10
            x = x // 10
            rev = rev * 10 + pop

        if rev > 2147483647:
            return 0

        else:

            if ind is False:
                rev = -rev

            return rev


Solution().reverse(1534236469)
