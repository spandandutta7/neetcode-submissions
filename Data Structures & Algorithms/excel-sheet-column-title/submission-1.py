class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1

            current = chr(ord("A") + (columnNumber%26))
            result.append(current)
            columnNumber = columnNumber // 26
        
        return "".join(reversed(result))


        