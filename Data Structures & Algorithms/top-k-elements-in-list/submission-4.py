from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        # O(n)
        for num in nums:
            counts[num] += 1 

        # O(n)
        reverse_counts = defaultdict(list)
        for key, value in counts.items():
            reverse_counts[value].append(key)

        # O(n)
        result = []
        for i in range(len(nums), 0, -1):
            if i not in reverse_counts:
                continue
            
            result.extend(reverse_counts[i])
            k -= len(reverse_counts[i])

            if k <= 0:
                break

        return result

        