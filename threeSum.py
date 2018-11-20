class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        n = len(nums)
        L_threesum = []
        L_twosum = []
        nums2 = nums.copy()
        for i in range(n-1):
            for j in range(i+1, n):
                twosum = nums[i] + nums[j]
                triplet = [nums[i], nums[j], -twosum]
                nums2.pop(j)
                nums2.pop(i)
                if -twosum in nums2:
                    unique_list = [[nums[i], nums[j]], [nums[j], nums[i]], [nums[i], -twosum], [nums[j], -twosum],
                                   [-twosum, nums[i]], [-twosum, nums[j]]]
                    ind = all([unique_list[_] not in L_twosum for _ in range(6)])
                    if ind:
                        L_threesum.append(triplet)
                        L_twosum.append([nums[i], nums[j]])
                nums2 = nums.copy()
        return L_threesum
        '''
        if len(nums) < 3:
            return []

        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res


Solution().threeSum([-7,-10,-1,3,0,-7,-9,-1,10,8,-6,4,14,-8,9,-15,0,-4,-5,9,11,3,-5,-8,2,-6,-14,7,-14,10,5,-6,7,11,4,-7,11,11,7,7,-4,-14,-12,-13,-14,4,-13,1,-15,-2,-12,11,-14,-2,10,3,-1,11,-5,1,-2,7,2,-10,-5,-8,-10,14,10,13,-2,-9,6,-7,-7,7,12,-5,-14,4,0,-11,-8,2,-6,-13,12,0,5,-15,8,-12,-1,-4,-15,2,-5,-9,-7,12,11,6,10,-6,14,-12,9,3,-10,10,-8,-2,6,-9,7,7,-7,4,-8,5,-4,8,0,3,11,0,-10,-9])

