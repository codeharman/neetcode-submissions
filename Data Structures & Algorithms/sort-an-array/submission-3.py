class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, fir, sec):
        final = []
        i = 0
        j = 0

        while i < len(fir) and j < len(sec):
            if fir[i] < sec[j]:
                final.append(fir[i])
                i += 1
            else:
                final.append(sec[j])
                j += 1
        
        final.extend(fir[i:])
        final.extend(sec[j:])

        return final

