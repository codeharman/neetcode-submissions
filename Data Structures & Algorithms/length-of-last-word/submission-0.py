class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.strip().split(" ")
        return len(result[-1])