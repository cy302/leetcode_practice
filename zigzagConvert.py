class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows == 0 or s is None:
            return s
        rstr = ''
        for i in range(numRows):
            if i == 0:
                rstr += s[::(2*numRows-2)]
            elif i == numRows-1:
                rstr += s[i::(2*numRows-2)]
            else:
                spacea = 2*(numRows-1-i)
                spaceb = 2*i
                counter = 0
                j = i
                while j < len(s):
                    rstr += s[j]
                    if counter % 2 == 0:
                        j += spacea
                    else:
                        j += spaceb
                    counter += 1
        return rstr


Solution().convert(s, 4)
