class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):

            if not stack or temperatures[stack[-1]] >= temp:
                stack.append(index)
            else:

                while stack and temperatures[stack[-1]] < temp:
                    result[stack[-1]] = index - stack[-1]
                    stack.pop()
                stack.append(index)
        

        return result


