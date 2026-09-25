class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "|" + s
            
        return result

    def decode(self, s: str) -> List[str]:  
        result = []
        l, r = 0, 0

        while l < len(s):
            while s[r] != "|":
                r += 1

            # r now holds the index of the separator
            length = int(s[l:r])

            start, end = r+1, r+1+length
            result.append(s[start:end])

            l, r = end, end

        return result

            