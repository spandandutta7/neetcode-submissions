class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(math.sqrt(num)) * int(math.sqrt(num)) == num

        