class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        i = 0
        # Iterates over char, only t, incrementing i everytime a matching character is found
        for char in t:
            if char == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False