class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ss1=sorted(s1)
        for i in range(len(s2)-len(s1)+1):
            j=i+len(s1)
            ss2=sorted(s2[i:j])
            if ss1==ss2:
                return True
        return False
