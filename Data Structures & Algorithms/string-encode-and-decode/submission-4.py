class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""

        for s in strs:
            res+=str(len(s))+"#"+s

        # 5#Hello5#world
        return res

    def decode(self, s: str) -> List[str]:

        res,i=[],0
        while i<len(s):
            number=int(s[i])
            word=""
            j=i
            while j<i+number:
                word+=s[j+2]
                j+=1
            print(word,"=-=-")
            res.append(word)
            i=i+number+2
            print(i)
        return res
