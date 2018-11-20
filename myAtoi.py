class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums = ["%s" % i for i in range(10)]

        if str == '':
            return 0
        elif len(str) == 1:
            if str in nums:
                return int(str)
            else:
                return 0
        else:

            i = 0
            while str[i] == ' ' and i < len(str)-1:
                i += 1

            if i == len(str) - 1 and str[-1] in nums:
                return int(str[-1])
            elif i == len(str) - 1 and str[-1] not in nums:
                return 0
            elif str[i] not in nums and str[i] != '-' and str[i] != '+':
                return 0
            else:
                integer = ''
                if str[i] in nums or str[i] == '-' or str[i] == '+':
                    integer += str[i]
                    i += 1
                    while str[i] in nums and i < (len(str)-1):
                        integer += str[i]
                        i += 1
                    if i == len(str)-1 and str[-1] != ' ' and str[-1] in nums:
                        integer += str[-1]
                    if integer == "+" or integer == "-":
                        return 0
                    integer = int(integer)
                    if integer > 2**31-1:
                        integer = 2**31-1
                    elif integer < -2**31:
                        integer = -2**31
                    else:
                        pass
                    return integer


Solution().myAtoi("+-2")
