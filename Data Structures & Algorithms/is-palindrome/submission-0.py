class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = [char.lower() for char in s if char.isalnum()]

        l = 0 
        r = len(c) - 1

        while l < r:
            if c[l] != c[r]:
                return False
            l += 1
            r -= 1
        return True
        
        