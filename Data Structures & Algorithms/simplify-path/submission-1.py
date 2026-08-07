class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splitStr = path.split("/")

        for seq in splitStr:
            if seq:
                if seq == "..":
                    if stack:
                        stack.pop()
                elif seq != ".":
                    stack.append(seq)
            
        return "/"+ "/".join(stack)
                 