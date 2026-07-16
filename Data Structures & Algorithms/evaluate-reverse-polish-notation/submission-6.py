import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_mapping = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}
        stack = []
        for ch in tokens:
            if ch in '+-/*':
                a_1 = stack.pop()
                a_2 = stack.pop()
                stack.append(int(operator_mapping[ch](a_2,a_1)))
            else:
                stack.append(int(ch))
        return stack.pop()
