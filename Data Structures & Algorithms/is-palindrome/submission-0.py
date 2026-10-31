class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(char.lower() for char in s if char.isalnum())
        print(a)
        i,j=0,len(a)-1
        while i < (len(a)//2):
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        return True