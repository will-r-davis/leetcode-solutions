class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1: 
            return nums[0]
        i = 0
        nums = [x/k for x in nums]
        maxAverage = -math.inf

        # Priming while loop with first sum value
        curAverage = sum(nums[i:(i+k-1)])
        prev = 0
        
        while i <= len(nums) - k:
            curAverage = curAverage - prev + nums[i + k - 1]
            maxAverage = max(maxAverage, curAverage)
            prev = nums[i]
            i += 1
        return maxAverage
        
        