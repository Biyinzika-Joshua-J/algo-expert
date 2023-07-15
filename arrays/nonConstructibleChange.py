def nCC(coins): # return minimum amount of change you can't create.. 
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return -1

"""
[7] => 1
[1,2,5] => 4
"""
coinValues = [5,7,1,1,2,3,22] # => 20
print(nCC(coinValues))