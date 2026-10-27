class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = []
        nums.sort()
        for i in nums:
            if i in k:
                return True
            else:
                k.append(i)
        return False