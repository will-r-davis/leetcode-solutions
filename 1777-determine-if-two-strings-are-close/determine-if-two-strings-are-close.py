class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = Counter(word1)
        dict2 = Counter(word2)
        occurences1 = sorted(list(dict1.values()))
        occurences2 = sorted(list(dict2.values()))
        if occurences1 != occurences2:
            return False
        elif set(dict1.keys()) != set(dict2.keys()):
            return False
        return True
