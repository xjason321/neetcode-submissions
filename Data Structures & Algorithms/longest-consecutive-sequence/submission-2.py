class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        First, find list of candidates (nums that don't have num - 1 in lookup). Then build sequence for 
        each. This avoids extra work.

        Creating hashset is O(n)
        Getting candidates is O(n)
        Getting max sequence is O(n)

        So total is O(3 * n) = O(n)
        """
        lookup = {}

        for num in nums:
            lookup[num] = True

        candidates = {}

        for num in lookup:
            if num-1 not in lookup:
                candidates[num] = True

        print(candidates)

        max_length = 0

        for candidate in candidates:
            length = 1
            while candidate+length in lookup:
                length += 1
            
            max_length = max(max_length, length)

        return max_length