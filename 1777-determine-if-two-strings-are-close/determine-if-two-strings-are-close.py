class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        This solution uses two dictionaries created for each string where keys are unique characters 
        and values are their frequency within the word. For two words to be close, 
        a set of their keys will be identical as will be a sorted list of their values.
        """
        # constructing dictionaries
        dict1 = Counter(word1)
        dict2 = Counter(word2)
        # comparing both sorted lists of occurences
        if sorted(list(dict1.values())) != sorted(list(dict2.values())):
            return False
        # comparing both sets of unique chars
        elif set(dict1.keys()) != set(dict2.keys()):
            return False
        return True
