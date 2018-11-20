class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits or digits == '':
            return []

        d = dict(zip(list('23456789'),'abc def ghi jkl mno pqrs tuv wxyz'.split()))
        res = ['']
        for digit in digits:
            res = [pre + curr for pre in res for curr in d[digit] if digit in d]
        return res


Solution().letterCombinations('23')


digits = '23'
list(itertools.product([d[i] for i in digits if i in d]))


def one_line_letter_comb(digits):
    d = dict(zip(list('23456789'), 'abc def ghi jkl mno pqrs tuv wxyz'.split(' ')))
    return [''.join(x) for x in itertools.product(*(d[i] for i in digits if i in digits))]
