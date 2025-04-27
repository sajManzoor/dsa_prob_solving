"""
28. Find the Index of the First Occurrence in a String
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return 0


        if needle in haystack:
            return haystack.index(needle)

        else:
            return -1

