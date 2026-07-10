class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += (str(len(i)) + "#"+ i)
        return ans
    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            j = i
            while s[j].isdigit():
                j += 1
            length = int(s[i:j])
            j += 1
            word = s[j:j + length]
            answer.append(word)
            i = j + length
        return answer