from typing import List

# Top K Frequent Elements
#
# Given an integer array nums and an integer k, return the k most frequent elements. 
# Return the answer in any order.
#
# Count number frequencies in a hash table, then create a list of lists where indices are frequencies 
# and elements are each unique number. Iterate backwards through that list, adding each number 
# to a result list until k have been found.
# Big-O:
# Time: O(n)
# Space: O(n)
#
# Alternatively, use a heap, but time complexity is worse: O(n log n). Or O(n log k) if heap 
# is popped whenever its size is over k.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Step 2: Create a list of lists where indices are frequencies
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        
        # Step 3: Iterate backwards through the frequency list and collect results
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
