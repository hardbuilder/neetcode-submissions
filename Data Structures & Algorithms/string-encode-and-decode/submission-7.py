class Solution:

    def encode(self, strs: List[str]) -> str:
        es=''
        for w in strs:
            es+=w+'≈'
        return es



    def decode(self, s: str) -> List[str]:
        es=[]
        b=''
        for w in s:
            if w=='≈':
                es.append(b)
                b=''
            else:
                b+=w
        return es