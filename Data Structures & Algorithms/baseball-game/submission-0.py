class Solution:
    def calPoints(self, operations: List[str]) -> int:

        score = 0
        stack = []
        for op in operations:
                
            if op == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
            elif op == "D":
                score = 2 * stack[-1]
                stack.append(score)
            elif op == "C":
                stack.pop()
            else:
                #score = op
                stack.append(int(op))

        total = sum(stack)
        #return sum(stack) if len(stack) > 0 else 0
        return total
