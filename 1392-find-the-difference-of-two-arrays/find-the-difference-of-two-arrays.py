class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1 = set([x for x in nums1 if x not in nums2])
        answer2 = set([x for x in nums2 if x not in nums1])
        return [answer1, answer2]