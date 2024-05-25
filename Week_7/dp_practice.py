def fibo(n):
    if n<= 1:
        return n
    
    a,b = 0, 1

    for i in range(2,n+1):
        a, b = b, b+a
    

    return b


if __name__ == '__main__':

    print(fibo(7))

