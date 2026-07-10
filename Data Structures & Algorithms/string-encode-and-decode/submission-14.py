class Solution:
    def encode(self, strs: List[str]) -> str:
        single = ""
        for i in strs:
            single += (str(len(i)) + "$" + i)
        return single
    def decode(self, s: str) -> List[str]:
        decoded = []
        pointer = 0
        grabbed = ""
        while pointer < len(s):
            grabbed = ""
            if pointer == len(s):
                return decoded
            while s[pointer].isdigit():
                grabbed += s[pointer]
                if pointer == len(s):
                    break
                else:
                    pointer += 1
            if (grabbed != "") and (s[pointer] == "$"):
                pointer += 1
                length = int(grabbed)
                decoded.append(s[pointer:pointer+length])
                grabbed = ""
                pointer += length
            else:
                pointer += 1
        return decoded