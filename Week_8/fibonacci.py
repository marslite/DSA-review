def fibonacci(n):
    if n == 0 or n ==1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


def efficient_Fibo(n, dict,memo):
    if n in memo:
        return memo[n]
    # else:
    #     memo[n] = 1

    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
    if n == 0 or n ==1:
        return 1
    current_n =  efficient_Fibo(n-1, dict,memo) + efficient_Fibo(n-2,dict,memo)
    memo[n] = current_n
    return memo[n]


def fibonacci_bottomUp(n):
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp)
    return dp[n]
            




    




# 0 -> 1 
# 1 -> 2 
#  3 -> 5





if __name__ == "__main__":
    dict = {}
    memo = {}
    print('Fibonacci')
    print(fibonacci(4))
    print(efficient_Fibo(4,dict,memo))
    print(fibonacci_bottomUp(4))