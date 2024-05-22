def fibonacci(n):
    if n == 0:
        return 0
    
    dp= [0] * (n+1)
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    
    # print(dp)
    
    return dp[n]


def fibRec(n):
    if n == 0:
        return 0;

    if n ==1:
        return 1
    
    return fibRec(n-1) + fibRec(n-2)



if __name__ == "__main__":
    # f(n) = f(n-1) + f(n-2) 
    print(fibonacci(7))

    # for i in range(11):
    #     print(fibonacci(i))
    
    # print(fibRec(50),"<--")