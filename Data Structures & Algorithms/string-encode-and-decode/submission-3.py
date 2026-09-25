class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "|" + s
            
        return result

    def decode(self, s: str) -> List[str]:  
        print(f"received: {s}")

        result = []
        l, r = 0, 0
        while l < len(s):
            print("iter start", l, r)

            while s[r] != "|":
                r += 1
            
            print("separator found, r set to", r)

            # r now holds the index of the separator
            length = int(s[l:r])

            print("got length", length)

            #  s  e
            # |cat  

            start, end = r+1, r+1+length # technically 

            print("using start, end:", start, end)

            result.append(s[start:end])

            print(s[start:end])

            l, r = end, end

        return result

            