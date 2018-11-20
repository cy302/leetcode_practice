class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
        	return 1
        if n < 0:
        	x = 1/x
        	n = -n
        half = self.myPow(x, n//2)
        if not n%2:
        	return half*half
        else:
        	return half*half*x


print(Solution().myPow(2, -4))
