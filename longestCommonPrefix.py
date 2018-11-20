class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''

        l = [len(strs[i]) for i in range(len(strs))]
        min_ind = l.index(min(l))
        shortest_str = strs[min_ind]
        if shortest_str == '':
            return ''
        common_prefix = ''
        ind = True
        i = 0
        while ind and i < l[min_ind]:
            prefix = shortest_str[i]
            ind = all([strs[j][i] == prefix for j in range(len(strs))])
            i += 1
        if i == l[min_ind] and ind == True:
            common_prefix += shortest_str[:i]
        else:
            common_prefix += shortest_str[:i-1]
        return common_prefix

    def BinarySearchLCP(self, strs):
        if not strs:
            return ''
        minLen = min([len(strs[i]) for i in range(len(strs))])
        low = 1
        high = minLen
        while low <= high:
            middle = (low+high)//2
            if Solution().isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle-1
        return strs[0][:(low+high)//2]

    def isCommonPrefix(self, strs, l):
        str1 = strs[0][:l]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True


Solution().longestCommonPrefix(['a', 'b'])
strs = ['a', 'b']
Solution().BinarySearchLCP(["flower", "flow", "flight"])
