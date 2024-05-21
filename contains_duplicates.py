from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


  # Algorithm:
        # 1- We start with an empty set called hashset. The empty set (or hashset) is used to keep track of unique numbers encountered so far in the input array nums.
        # 2- We go through each number n in the input array nums.
        # 3- For each number n, we check if it's already in the hashset.
        #    - If it is, then we've found a duplicate, so we return True.
        #    - If it's not, we add n to the hashset.
        # 4- If we finish going through all numbers in nums without finding any duplicates, we return False because there are no duplicates.
        #
        # Big-O:
        # Time: O(n)
        # Space: O(n)