class Solution:
    def scoreOfString(self, s: str) -> int:
        result = [ord(char) for char in s]
        ans = 0
        for i in range(len(result)-1):
            ans += abs(result[i + 1] - result[i])
            
        return ans 