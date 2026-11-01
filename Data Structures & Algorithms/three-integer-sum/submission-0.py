class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                m = [nums[i],nums[j],nums[k]]
                m.sort()
                if m not in res and sum(m)==0:
                    res.append(m)
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
        return res