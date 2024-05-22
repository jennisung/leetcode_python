# Valid Anagram
# 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram" 
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car" 
# Output: false
#
# Algorithm:
# Sort the input strings:
# Sort the characters of both strings s and t.
# For example, if s = "anagram" and t = "nagaram", after sorting, sorted_s = "aaagmnr" and sorted_t = "aaagmnr".
# Compare the sorted strings:
# If the sorted strings are equal, return True, indicating that s and t are anagrams.
# Otherwise, return False, indicating that s and t are not anagrams.
#
# Big-O:
# Time: O(n log n)
# Space: O(n)



# Algorithm
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

# Example:
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))  # Output: True
    print(solution.isAnagram("rat", "car"))  # Output: False
