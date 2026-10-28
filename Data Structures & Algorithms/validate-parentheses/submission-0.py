class Solution:
    def isValid(self, s: str) -> bool:
        maps = {'}':'{',']':'[',')':'('}
        stack=[]
        for i in s:
            if stack and i in maps and maps[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False