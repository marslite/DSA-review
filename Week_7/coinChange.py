
def coinChange( coins: list[int], amount:int) -> int:

    memo = [float("inf")] * (amount+1)
    memo[0] = 0
    for sa in range(1,amount+1):
        for coin in coins:
            if (sa - coin) >= 0:
                memo[sa] = min(memo[sa], memo[sa-coin]+1)
    
    return memo[amount] if memo[amount] != float("inf") else -1





if __name__ == "__main__":
    coins = [1,3,4,5]
    print(coinChange(coins, 7))




