class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k = list(sorted(set(nums)))
        if len(k)==0 or len(k)==1:
            return len(k)
        a = []
        count=0
        for i in range(len(k)-1):
            if k[i]==k[i+1]-1:
                count+=1
            else:
                a.append(count+1)
                count=0
        if a and max(a)>count+1:
            return max(a)
        else:
            return count+1