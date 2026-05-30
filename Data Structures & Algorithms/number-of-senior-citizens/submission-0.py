class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for i in details:
            age = int(i[-4:-2])
            if age > 60:
                counter += 1
        return counter