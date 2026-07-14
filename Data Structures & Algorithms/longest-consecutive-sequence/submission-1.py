class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()
        pin, strk = nums[0], 0
        i = 0
        while i < len(nums):
            if pin != nums[i]:
                pin = nums[i]
                strk = 0
            while i < len(nums) and nums[i] == pin:
                i += 1
            strk += 1
            pin += 1
            res = max(res, strk)
        return res
