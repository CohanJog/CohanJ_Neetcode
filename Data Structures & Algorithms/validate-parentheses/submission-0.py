class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_pairs = {')': '(', ']': '[', '}': '{'}

        for character in s:
            if character in '([{':
                stack.append(character)
            else:
                if not stack or stack.pop() != paren_pairs[character]:
                    return False
        return len(stack) == 0