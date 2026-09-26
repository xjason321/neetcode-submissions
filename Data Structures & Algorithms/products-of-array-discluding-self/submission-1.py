class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Strategy: memoize the products, we'll form a 2 x n array
        |  |  |  |  |  |  |  |  <- collects from 0...i
        |  |  |  |  |  |  |  |  <- collects from i...n
        This can be calculated in two iterations of nums
        """
        
        lookup_l = [0] * len(nums)
        lookup_r = [0] * len(nums)

        product = 1
        for i in range(len(nums)):    
            product *= nums[i]
            lookup_l[i] = product

        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            lookup_r[i] = product

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(lookup_r[i+1])
            elif i == (len(nums)-1):
                output.append(lookup_l[i-1])
            else:
                output.append(lookup_l[i-1] * lookup_r[i+1])

        return output

        """
        O(n^2) solution

        output = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j: continue
                product *= nums[j] 
            output.append(product)
        
        return output
        """