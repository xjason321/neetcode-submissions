class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_lookup = {}

        for i, num in enumerate(nums):
            if num in target_lookup:
                return [target_lookup[num], i]
            else:
                target_lookup[target - num] = i

        return None