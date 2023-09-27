"""
    target => amount of money
    coins => array of coin denominations
    find minimum number of coins needed to reach the target amount
    Assume we have an infinite number of coins
"""

def min_num(target, coins):
    numOfCoins = [float('inf') for amount in range(0, target+1)]
    numOfCoins[0] = 0
    for coin in coins:
        for amount, num in enumerate(numOfCoins):
            if coin <= amount: 
                numOfCoins[amount] = min(numOfCoins[amount], 1+numOfCoins[amount-coin])
    return numOfCoins[-1]


print(min_num(6, [1,2,4])) # 2 coins 2+4