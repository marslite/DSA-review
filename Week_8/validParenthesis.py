

#Output: true
#stack = ['{']
#val = [ ']' ]
def validParenthesis(s):
    parens = ['(',')','[',']']
    stack = []
    for c in s:
        idx = parens.index(c)
        if idx % 2 == 0:
            stack += c
        else:
            if len(stack) == 0:
                return False
            val = stack.pop()
            if parens[idx-1] != val:
                return False
    if not stack:
        return True
    return False
            


if __name__ == "__main__":
    print("Valid Parenthesis")
    invalid_s = "(()()"
    print(validParenthesis(invalid_s))
