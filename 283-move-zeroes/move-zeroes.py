class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        writeIndex = i = 0
        writeValue = nums[0]
        while i < len(nums):
            
            #Iterating over nums until a non-zero value is found
            while i < len(nums) and nums[i] == 0:
                i += 1

            #Recording next non-zero value in 'writeValue'
            if i < len(nums):
                writeValue = nums[i]

                #Writing found non-zero value to it's final index
                nums[writeIndex] = writeValue
                writeIndex += 1
            i += 1

        #Placing zeros at end of dataful list
        while writeIndex < len(nums):
            nums[writeIndex] = 0
            writeIndex += 1

        """
        Do not return anything, modify nums in-place instead.
        """
        