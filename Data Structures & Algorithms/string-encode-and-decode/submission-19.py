class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = str(hash("MySecretEncoding!"))
        temp = ""
        for i in strs:
            temp += i + encoding
        return temp

    def decode(self, s: str) -> List[str]:
        ret = s.split(str(hash("MySecretEncoding!")))
        return ret[:-1]