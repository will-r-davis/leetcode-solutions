class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Solution with two pointers conditionally moving inward over a sorted version of nums
        Second submission adds second check for loop condition, paring unnecessary interations
        """

        nums.sort()
        i = operations = 0
        j = len(nums) - 1
        while i < j and nums[i] < k:
            cur = nums[i] + nums[j]
            if cur == k:
                operations += 1
                i += 1
                j -= 1
            elif cur < k:
                i += 1
            else:
                j -= 1
        return operations