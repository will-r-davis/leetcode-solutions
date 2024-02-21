class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        writeIndex = 0
        for i in range(len(nums)):
            
            #Checking for non-zero value, and writing it to it's correct index
            if nums[i] != 0:
                nums[writeIndex] = nums[i]
                writeIndex += 1

        #Placing zeros at end of dataful list
        while writeIndex < len(nums):
            nums[writeIndex] = 0
            writeIndex += 1
        