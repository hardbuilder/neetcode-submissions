class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {k:i for i,k in enumerate(nums)}
        for i in range(len(nums)):
            p=nums[i]
            if target-p in d and i!=d[target-p]:
                return [i,d[target-p]]