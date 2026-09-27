class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Iterate through nums, creating a hash map and storing the min value and max value,
        Then, 
            - let remaining = len(nums)            
            - max_consecutive = 0
        start at the min value and and consecutively lookup min + 1 
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
                

            

                
        
        return max(lengths.values())