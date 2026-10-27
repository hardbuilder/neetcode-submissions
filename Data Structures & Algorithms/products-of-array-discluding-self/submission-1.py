from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j=[1]*len(nums)
        pf=1
        sf=1
        for i in range(len(nums)):
            j[i]=pf
            pf*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            j[i]*=sf
            sf*=nums[i]
        return j