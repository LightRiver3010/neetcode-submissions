class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        hashing = hash("test")
        for s in strs:
            newStr += s + str(hashing)
        return newStr

    def decode(self, s: str) -> List[str]:
        strs = s.split(str(hash("test")))
        return strs[:-1]