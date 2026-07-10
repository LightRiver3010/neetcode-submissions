class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        shortest = strs[0]
        current_str = ""
        current_index = 0
        while current_index < len(shortest):
            for i in strs:
                if i[current_index] != shortest[current_index]:
                    return current_str
            current_str += shortest[current_index]
            current_index += 1
        return current_str