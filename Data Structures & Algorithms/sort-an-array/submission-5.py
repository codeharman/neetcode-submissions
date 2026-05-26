class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        
        left = self.sortArray(nums[mid:])
        right = self.sortArray(nums[:mid])

        return self.merge(left, right)

    def merge(self, first, second):
        final = []
        i = 0
        j = 0

        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1
        
        final.extend(first[i:])
        final.extend(second[j:])

        return final
            