
def factorial(n):
    if n == 1:
        return 1
    #Runtime O(n)
    #Space O(n)
    return factorial(n-1) * n




def iterative(n):
    sol = 1
    for i in range(1,n+1):
        sol *= i
    #Runtime O(n)
    #Space O(1)
    return sol
    

if __name__ == "__main__":
    print("lol")
    print(factorial(5))
    print(iterative(5))