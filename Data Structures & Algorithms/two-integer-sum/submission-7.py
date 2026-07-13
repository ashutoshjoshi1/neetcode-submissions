class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums[i+1:]:
        #         a = i
        #         nums.remove(nums[i])
        #         b = nums.index(diff)+1
        #         return [a,b]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
        