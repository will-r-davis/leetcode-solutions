class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = list(Counter(arr).values())
        return len(set(occurences)) == len(occurences)
