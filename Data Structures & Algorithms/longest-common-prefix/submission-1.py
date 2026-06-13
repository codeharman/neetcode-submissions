class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        sorted_array = sorted(strs)

        for i in range(min(len(sorted_array[0]), len(sorted_array[-1]))):
            if sorted_array[0][i] != sorted_array[-1][i]:
                return sorted_array[0][:i]

        return sorted_array[0]