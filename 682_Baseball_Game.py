class Solution(object):
    def calPoints(self, operations):
        '''first attempt'''
        stack = []

        for v in operations:
            if v == '+':
                stack.append(int(stack[-2])+int(stack[-1]))
            elif v == 'D':
                stack.append(int((stack[-1])*2))
            elif v == 'C':
                stack.pop()
            else:
                stack.append(int(v))
        
        total_sum = 0

        for value in stack:
            total_sum += int(value)

        return total_sum

        '''modified way'''
                
        stack = []
        for v in operations:
            if v == '+':
                stack.append(stack[-1] + stack[-2])
            elif v == 'D':
                stack.append(2 * stack[-1])
            elif v == 'C':
                stack.pop()
            else:
                stack.append(int(v))
        
        return sum(stack)
        # return sum(int(value) for value in stack)