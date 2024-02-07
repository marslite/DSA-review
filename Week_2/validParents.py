def validParens(s):
    #Runtime Complexity O(N)
    #Space Complexity  O(N) We're adding to our stack depending by N size, so O(N)
    parens = ['(',')','[',']','{', '}']
    stack = []
    #O(N) Iterating N times 
    for c in s:
        #Looking for index of x is O(1)
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

