class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def NSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < N*nums[0] or target > N*nums[-1]:
                return []
            if N == 2:
                l, r = 0, len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result+[nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

            else:
                for i in range(len(nums)-N+1):
                    if (i > 0 and nums[i] == nums[i-1]) or (nums[i] + (N-1)*nums[-1] < target):
                        continue
                    if N*nums[i] > target:
                        break
                    if N*nums[i] == target and i+N-1 < len(nums) and nums[i+N-1] == nums[i]:
                        results.append(result+N*[nums[i]])
                        break
                    NSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        nums.sort()
        NSum(nums, target, 4, [], results)
        return results


Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
nums = [1, 0, -1, 0, -2, 2]
