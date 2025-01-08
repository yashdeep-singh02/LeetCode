class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current=0
        max_altitude=0
        for g in gain:
            current=current+g
            if current>max_altitude:
                max_altitude=current
            
        return max_altitude
        