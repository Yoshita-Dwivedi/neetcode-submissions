class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map = {}

        for ch in s:
            freq_map[ch] = freq_map.get(ch,0) + 1

        for ch in t:
            if ch not in freq_map:
                return False
            if freq_map[ch] == 0:
                return False
            freq_map[ch] -= 1
    
        for value in freq_map.values():
            if value != 0:
                return False
        return True

        
        