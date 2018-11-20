class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_letter = set([w for w in s])
        s_dict = dict.fromkeys(s_letter, -1)
        tmp_len = 0
        record_len = 0
        start_point = -1
        for i, le in enumerate(s):
            tmp_point = s_dict[le]
            if tmp_point <= start_point:
                s_dict[le] = i
                tmp_len += 1
            else:
                start_point = tmp_point
                s_dict[le] = i
                if tmp_len > record_len:
                    record_len = tmp_len
                tmp_len = i-tmp_point
        if tmp_len > record_len:
            record_len = tmp_len
        return record_len


Solution().lengthOfLongestSubstring("anviaj")
