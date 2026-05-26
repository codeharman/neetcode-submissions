class Solution:
    def reverseString(self, s: List[str]) -> None:
        reversed = []
        for i in range(len(s) - 1, -1, -1):
            reversed.append(s[i])

        for x in range(len(s)):
            s[x] = reversed[x]
        