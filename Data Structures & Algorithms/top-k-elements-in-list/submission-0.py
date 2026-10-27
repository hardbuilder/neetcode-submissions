from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        a = []
        for i in d.most_common(k):
            a.append(i[0])
        return a
