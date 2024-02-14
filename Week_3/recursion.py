

#This would run untill negative infinity.
# What we need to avoid to recursively call the function to negative infinity
# is a base case 
def infinite_recursion_no_base_case(n):
    print(n)
    infinite_recursion_no_base_case(n-1)

#This would be a proper way to recursively call a function untill we reach the baes case.
    
def proper_recursion(n):
    if(n==0):
        return
    print(n)
    return proper_recursion(n-1)

def factorial(n):
    if n == 0 or n ==1:
        return 1
    print(n, "* ",n-1, "=", (n-1) *n)

    return factorial(n-1)*n




def fib(n,dict):
    if n in dict:
        dict[n] +=1
    else:
        dict[n] = 1

    if(n==0 or n==1):
        return 1
    
    return fib(n-1,dict) + fib(n-2,dict)

def fibMemo(n, dict,memo):
    #Runtime Complexity O(N)
    #Space Complexity O(N)
    if n in memo:
        return memo[n]

    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1

    if(n==0 or n==1):
        return 1

    current_n = fibMemo(n-1,dict,memo)+fibMemo(n-2,dict,memo)
    memo[n] = current_n
    return current_n


def fibBottomUp(n):
    #Runtime Complexity O(N)
    #Space Complexity O(N)
    dp = [0]*(n+1)

    dp[0] = dp[1] = 1
    count = 2
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        count +=1
    print("fib Bottom Up Stack Call", count)
    return dp[-1]



if __name__ == "__main__":

    # infinite_recursion_no_base_case(10)
    # proper_recursion(10)
    # print(factorial(5))
    # print(fib(10))

    d ={}
    q ={}
    memo = {}
    n = 4



    print("Result: ", fib(n,d),"Stack calls: ", sum(d.values()))

    print("Result: ",fibMemo(n,q,memo), "Stack calls with Memo: ", sum(q.values()))

    fb = fibBottomUp(n)



