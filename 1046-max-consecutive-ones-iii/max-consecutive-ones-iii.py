class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Edge case code for singleton/empty list
        if len(nums) <= k:
            return len(nums)

        maxCount = 0
        curCount = 0
        zeroes = 0
        left = 0


        for right in range(len(nums)):

            # right pointer encounters 1
            if nums[right] == 1:
                curCount += 1
                maxCount = max(maxCount, curCount)

            # right pointer encounters 0
            else:    
                zeroes += 1

                # number of zeroes in slice is less than number of flips
                if zeroes <= k:
                    curCount += 1
                    maxCount = max(maxCount, curCount)

                # number of zeroes in slice exceeds number of flips
                else:
                    # incrementing left pointer to position of first 0 in slice
                    while left < right and nums[left] == 1:
                        curCount -= 1
                        left += 1
                    # removing zero from beginning of slice
                    zeroes -= 1
                    left += 1

        return maxCount

