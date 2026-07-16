class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'}':'{', ']':'[', ')':'('}
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if hashmap[ch] != stack.pop():
                    return False

        return len(stack) == 0
                