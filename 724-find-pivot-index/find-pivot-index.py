class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rSum = sum(nums)
        lSum = 0
        for i in range(len(nums)):
            rSum -= nums[i]
            if rSum == lSum:
                return i
            lSum += nums[i]
        return -1
        