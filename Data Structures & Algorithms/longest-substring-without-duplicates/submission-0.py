class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        a=set()
        i=0
        for j in range(len(s)):
            while s[j] in a:
                a.discard(s[i])
                i+=1
            a.add(s[j])
            length=len(a) if len(a)>length else length
        return length
