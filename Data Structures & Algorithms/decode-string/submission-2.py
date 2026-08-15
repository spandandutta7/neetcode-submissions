class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        i = 0
        for char in s:
            if char == "]":
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                
                mult = ""
                while stack and stack[-1].isdigit():
                    mult = stack.pop() + mult
                stack.append(int(mult) * substring)

            else:
                stack.append(char)
        
        return "".join(stack)



        