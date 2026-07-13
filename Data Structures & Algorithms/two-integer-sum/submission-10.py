class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums[i+1:]:
        #         a = i
        #         nums.remove(nums[i])
        #         b = nums.index(diff)+1
        #         return [a,b]

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        # A = []
        # for i, num in enumerate(nums):
        #     A.append([num, i])
        # A.sort()
        # i,j = 0, len(nums) - 1
        # while i < j:
        #     cur = A[i][0] + A[j][0]
        #     if cur == target:
        #         return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
        #     elif cur < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return []

        # indices = {} #val -> index
        # for i ,n in enumerate(nums):
        #     indices[n] = i
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in indices and indices[diff] != i:
        #         return [i, indices[diff]]
        # return []

        prev = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i
        