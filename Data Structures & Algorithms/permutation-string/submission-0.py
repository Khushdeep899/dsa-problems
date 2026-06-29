class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord('a')] += 1
        wind_size = len(s1)
        for i in range(len(s2)):
            wind_freq = [0] * 26
            wind_idx, idx = 0, i
            while wind_idx < wind_size and idx < len(s2):
                wind_freq[ord(s2[idx]) - ord('a')] += 1
                wind_idx += 1
                idx += 1
            if freq == wind_freq:          # list == is element-wise
                return True
        return False
        