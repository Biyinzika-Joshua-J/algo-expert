def balanced_brackets(input):
    brackets_mapping = {
        ']':'[',
        '}':'{',
        ')':'(',
    }
    stack = []
    opened_brackets = '[{('
    for bracket in input:
        if bracket in opened_brackets:
            stack.append(bracket)
        else:
            equivalent_opening_bracket = brackets_mapping[bracket]
            if len(stack) == 0:
                return False
            if equivalent_opening_bracket == stack[-1]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

input = '(([]()()){})' # true
print(balanced_brackets(input))