class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        After 15 minutes of consideration, I could not think of a solution better than O(n^2). 
        The following code will demonstrate a brute force approach
        examining each possible slice of the array to find the maximum area 
        """
        # xValue = len(height) - 1
        # maxArea = 0
        # while xValue > 0:
        #     i = 0
        #     j = xValue
        #     while j < len(height):
        #         yValue = min(height[i], height[j])
        #         maxArea = max (maxArea, xValue * yValue)
        #         i += 1
        #         j += 1
        #     xValue -= 1
        # return maxArea

        """
        When returning to this problem after some time I realized that a better solution exists. The solution involves a single while loop with a sliding window where where the lesser of the left and right pointers moves inwards on each iteration, until the pointers meet. This ensures that only windows that have a potential to have a greater area are examined.
        Refactoring my code in this way reduces the runtime from O(n^2) to O(n/2) == O(n)
        """
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            xValue = j - i
            yValue = min(height[i], height[j])
            maxArea = max (maxArea, xValue * yValue)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea
