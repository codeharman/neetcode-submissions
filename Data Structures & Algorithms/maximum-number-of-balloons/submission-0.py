class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = {}

        for i, char in enumerate(text):
            if char not in ans:
                ans[char] = 1
            else:
                ans[char] += 1
        
        return min(
            ans.get('b', 0),
            ans.get('a', 0),
            ans.get('l', 0) // 2,
            ans.get('o', 0) // 2,
            ans.get('n', 0)
        )