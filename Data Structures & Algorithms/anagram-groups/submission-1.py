from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i, s in enumerate(strs):
            anagrams[str(sorted(s))].append(s)

        result = []
        for key in anagrams:
            result.append(anagrams[key])

        return result
