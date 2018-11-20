 class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        res = ''
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max = 0
        for j in range(n):
            for i in range(0, j+1):
                dp[i][j] = (s[i] == s[j]) and ((j-i <= 2) or dp[i+1][j-1])
                if dp[i][j]:
                    if j-i+1 > max:
                        max = j-i+1
                        res = s[i:j+1]
        return res

    def Manacher(self, s):
        if len(s) <= 1:
            return s
        n = len(s)
        st = ''
        for i in range(n):
            st += '#' + s[i]
        st += '#'
        del n
        n = len(st)
        P = [0 for _ in range(n)]
        C, R = 1, 2
        P[1] = 1
        maxInd, maxCount = 0, 1
        for i in range(2, n):
            i_mirror = 2*C-i

            if R > i and P[i_mirror] < R-i:
                P[i] = P[i_mirror]
                continue

            count = min(i, n-i-1)

            for _ in range((1 if R <= i else R+1-i), count+1):
                if st[i+_] != st[i-_]:
                    count = n-1
                    break

            C = i
            R = i + count
            P[i] = count

            if count > maxCount:
                maxCount = count
                maxInd = i-count

        maxInd = maxInd//2
        return s[maxInd:maxInd+maxCount]

'''
            if i+P[i] >= R:
                C = i
                R = i+P[i]

        maxLen = 0
        center_ind = 0
        for i in range(n):
            if P[i] > maxLen:
                maxLen = P[i]
                center_ind = i

        maxPalin = s[int((center_ind-1-maxLen)/2):int((center_ind-1-maxLen)/2+maxLen)+1]

        return maxPalin
'''


Solution().longestPalindrome('cbbd')
Solution().Manacher('cbbd')
