class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = sorted(list(Counter(arr).values()))
        for i in range(len(occurences)-1):
            if occurences[i] == occurences[i+1]:
                return False
        return True
