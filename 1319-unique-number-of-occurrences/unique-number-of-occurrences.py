class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = sorted(list(Counter(arr).values()))
        return len(set(occurences)) == len(occurences)
