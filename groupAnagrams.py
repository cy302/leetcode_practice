class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
        	stv = ''.join(sorted(s))
        	if stv in d:
        		d[stv].append(s)
        	else:
        		d[stv] = [s]
        return list(d.values())


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
