class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rSum = sum(nums[1:])
        lSum = 0
        for i in range(len(nums)-1):
            if rSum == lSum:
                return i
            rSum -= nums[i+1]
            lSum += nums[i]
        if rSum == lSum:
                return len(nums)-1
        return -1
        