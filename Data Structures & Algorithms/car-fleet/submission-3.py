import math
from collections import defaultdict
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=[]
        stack=[]
        d=defaultdict(int)
        for i in range(len(position)):
            d[position[i]]=speed[i]
        d = dict(sorted(d.items(),reverse=True))
        for i,j in d.items():
            res.append((target-i)/j)
        for i in res:
            if stack:
                if stack[-1]<i:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)