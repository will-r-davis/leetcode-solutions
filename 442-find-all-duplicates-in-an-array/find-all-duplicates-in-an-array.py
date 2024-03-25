class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        def seen(i: int, nums: List[int]) -> bool:
            return nums[i] < 0

        result = []
        for num in nums:
            index = abs(num) - 1
            if seen(index, nums):
                result.append(index + 1)
            else:
                nums[index] *= -1

        return result
            