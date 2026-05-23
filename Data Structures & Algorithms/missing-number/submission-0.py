class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = range(0, len(nums) + 1)
        for i in seen:
            if i not in nums:
                return i