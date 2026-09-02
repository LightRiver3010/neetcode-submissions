class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for s in strs:
            newStr += str(len(s)) + "$" + s
        return newStr

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs = []
        C = 0
        word = ""
        leng = ""
        while C < len(s):
            leng = ""
            if s[C] == 0:
                strs.append("")
                C += 2
            else:
                while s[C] != "$":
                    leng += s[C]
                    C += 1
                leng = int(leng)
                word = s[C+1:C+1+leng]
                strs.append(word)
                C += 1 + leng
        return strs
