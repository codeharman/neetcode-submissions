class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for x,j in seen.items():
            if j <= 1:
                return x