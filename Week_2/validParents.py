def validParens(s):
    parens = ['(',')','[',']','{', '}']
    stack = []
    for c in s:
        idx = parens.index(c)
        if idx % 2 == 0:
            stack += c
        else:
            if len(stack) == 0:
                return False
            else:
                val = stack.pop()
                if val != parens[idx - 1]:
                    return False
                return True
            
    if(len(stack) == 0):
        return True
    return False




if __name__ == '__main__':
    s = "()"
    print(validParens(s))

    s1 = "()[]{}"
    print(validParens(s1))

    s2 = "(]"
    print(validParens(s2))

    s3 = "{[)}"
    print(validParens(s3))

    s4= "{[]}"
    print(validParens(s4))

