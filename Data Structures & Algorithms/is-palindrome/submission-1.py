class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = s.lower()
        copy = copy.strip() #Remove leading and trailing whitespace
        copy = copy.replace(" ", "") #Replacing whitespace with nothing
        if not copy.isalnum(): #Only needed if non-alnum characters exist; save time
            copyCopy = ""
            for character in copy:
                if character.isalnum():
                    copyCopy += character
            copy = copyCopy
        L = 0
        R = len(copy) - 1
        while L < R:
            if copy[L] != copy[R]:
                return False
            L += 1
            R -= 1
        return True