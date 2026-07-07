class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            # Store: length + '#' + string
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):

            # Find the '#'
            j = i
            while s[j] != "#":
                j += 1

            # Extract the length
            length = int(s[i:j])

            # Move pointer after '#'
            i = j + 1

            # Extract the actual string
            res.append(s[i:i + length])

            # Move pointer to next encoded string
            i = i + length

        return res
