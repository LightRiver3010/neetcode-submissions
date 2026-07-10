class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded = ""
        firstWord = strs[0]
        if len(firstWord) == 0:
            buffer = str(hash("LightRiver"))
        else:
            buffer = str(hash(firstWord[0]))
        for word in strs:
            encoded += word + buffer
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s.startswith(str(hash("LightRiver"))):
            buffer = str(hash("LightRiver"))
        else:
            buffer = str(hash(s[0]))
        ans = s.split(buffer)
        return ans[:-1]
