class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'i', 'o', 'u', 'e'])
        curCount = 0

        # Since the subsequent for loop references previous values, we prime    
        # curCount to be number of vowels in first slice of size 
        for char in s[0:k]:
            if char in vowels:
                curCount += 1
        maxCount = curCount
        # Looping through s with a window of size k, adding/subtracting 1 to curCount as vowels are encountered/passed
        for i in range(1, len(s) - k + 1):
            curCount = curCount - 1 if s[i-1] in vowels else curCount
            if s[i + k - 1] in vowels:
                curCount += 1
            i+=1
            maxCount = max(curCount, maxCount)

        return maxCount
        