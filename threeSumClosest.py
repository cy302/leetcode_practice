class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []

        diff = 2**31-1
        closest_sum = []
        nums.sort()

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff_temp = abs(s-target)
                if diff_temp < diff:
                    closest_sum = s
                    diff = diff_temp
                if s < target:
                    l += 1
                else:
                    r -= 1
                if closest_sum == target:
                    return closest_sum
        return closest_sum


Solution().threeSumClosest([1,1,-1,-1,3], target=-1)
