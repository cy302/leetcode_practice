class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1: return False
        d = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for char in s:
            if char in d:
                stack.append(char)
            else:
                if not stack or d[stack.pop()] != char:
                    return False
        return not stack


Solution().isValid("{[]}")
s = "{[]}"
