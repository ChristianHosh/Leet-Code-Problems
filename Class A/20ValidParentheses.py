class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                popped = stack.pop() if len(stack) != 0 else None
                if popped is not None:
                    if char == ')' and popped != '(':
                        return False
                    if char == '}' and popped != '{':
                        return False
                    if char == ']' and popped != '[':
                        return False
                else:
                    stack.append(char)

        return len(stack) == 0


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))



