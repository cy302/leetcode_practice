class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # rank = {'I': 0, 'V': 1, 'X': 2, 'L': 3, 'C': 4, 'D': 5, 'M': 6}
        value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)-1):
            if value[s[i]] < value[s[i+1]]:
                num -= value[s[i]]
            else:
                num += value[s[i]]
        num += value[s[-1]]
        return num


Solution().romanToInt("MCMXCIV")
