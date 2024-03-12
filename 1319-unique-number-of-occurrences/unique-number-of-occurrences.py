class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for x in arr:
            if x in occurences:
                occurences[x] += 1
            else:
                occurences[x] = 1
        
        v = sorted(list(occurences.values()))
        for i in range(len(v)-1):
            if v[i] == v[i+1]:
                return False
        return True
