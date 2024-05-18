from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.

        Algorithm:
        - Initialize an empty dictionary to store numbers and their indices.
        - Go through each number in the array and for each number in the array, check if the complement (target - number) is already in the dictionary.
            - If true, return the indices of both the current number and complement.
            - If false, add the current number to the dictionary with its index.
        - If there is no solution, return an indication that no solution exists.

        Time Complexity: O(n): linear
        Space Complexity: O(n): linear
        """
        prevMap = {}  # val -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


