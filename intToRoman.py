class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        '''
        # Now this is the smart way and even more universal, but in this case, int: 0-3999, it is faster to simply 
        # assign everything beforehand
        dict = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(dict, nums):
            result += letter * int(num / n)
            num %= n
        return result
        '''
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return M[((num // 1000) % 10)] + C[(num // 100) % 10] + X[(num // 10) % 10] + I[num % 10]
