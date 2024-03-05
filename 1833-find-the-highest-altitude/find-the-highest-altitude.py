class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        altitude = 0
        for x in gain:
            altitude += x
            if x > 0:
                maxAltitude = max(altitude, maxAltitude)
        return maxAltitude

